import os
import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.profiler import (
    profile,
    record_function,
    ProfilerActivity,
    schedule,
    tensorboard_trace_handler,
)


# -------------------------
# 1. VGG-like CNN model
# -------------------------

class ConvBNReLU(nn.Module):
    def __init__(self, in_channels, out_channels, name):
        super().__init__()
        self.name = name
        self.conv = nn.Conv2d(
            in_channels,
            out_channels,
            kernel_size=3,
            padding=1,
            bias=False,
        )
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        # 这里的 record_function 会在 profiler trace 里显示 layer 名称
        with record_function(f"{self.name}/conv"):
            x = self.conv(x)

        with record_function(f"{self.name}/bn"):
            x = self.bn(x)

        with record_function(f"{self.name}/relu"):
            x = self.relu(x)

        return x


class SmallVGG(nn.Module):
    """
    Input:  [N, 3, 32, 32]
    Output: [N, num_classes]
    """

    def __init__(self, num_classes=10):
        super().__init__()

        self.block1 = nn.Sequential(
            ConvBNReLU(3, 64, "block1/layer1"),
            ConvBNReLU(64, 64, "block1/layer2"),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.block2 = nn.Sequential(
            ConvBNReLU(64, 128, "block2/layer1"),
            ConvBNReLU(128, 128, "block2/layer2"),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.block3 = nn.Sequential(
            ConvBNReLU(128, 256, "block3/layer1"),
            ConvBNReLU(256, 256, "block3/layer2"),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256 * 4 * 4, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, num_classes),
        )

    def forward(self, x):
        with record_function("model/block1"):
            x = self.block1(x)

        with record_function("model/block2"):
            x = self.block2(x)

        with record_function("model/block3"):
            x = self.block3(x)

        with record_function("model/classifier"):
            x = self.classifier(x)

        return x


# -------------------------
# 2. Synthetic data
# -------------------------

def make_fake_batch(batch_size, device):
    images = torch.randn(batch_size, 3, 32, 32, device=device)
    labels = torch.randint(0, 10, (batch_size,), device=device)
    return images, labels


# -------------------------
# 3. Profiler setup
# -------------------------

def build_profiler(log_dir="./profiler_vgg_logs"):
    activities = [ProfilerActivity.CPU]

    if torch.cuda.is_available():
        activities.append(ProfilerActivity.CUDA)

    return profile(
        activities=activities,

        # 训练任务不要全程 profile，只采稳定窗口
        schedule=schedule(
            wait=2,
            warmup=2,
            active=6,
            repeat=1,
        ),

        # 输出 TensorBoard trace
        on_trace_ready=tensorboard_trace_handler(log_dir),

        # 调试信息
        record_shapes=True,
        profile_memory=True,
        with_stack=True,
        with_flops=True,
    )


# -------------------------
# 4. Training loop with profiler
# -------------------------

def run_profile():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    torch.manual_seed(0)

    model = SmallVGG(num_classes=10).to(device)
    model.train()

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()

    batch_size = 128
    num_steps = 16

    log_dir = "./profiler_vgg_logs"
    os.makedirs(log_dir, exist_ok=True)

    with build_profiler(log_dir) as prof:
        for step in range(num_steps):
            with record_function("data/create_fake_batch"):
                images, labels = make_fake_batch(batch_size, device)

            with record_function("train/zero_grad"):
                optimizer.zero_grad(set_to_none=True)

            with record_function("train/forward"):
                logits = model(images)

            with record_function("train/loss"):
                loss = criterion(logits, labels)

            with record_function("train/backward"):
                loss.backward()

            with record_function("train/optimizer_step"):
                optimizer.step()

            # 使用 schedule 时必须调用 step()
            prof.step()

    sort_key = "cuda_time_total" if torch.cuda.is_available() else "cpu_time_total"

    print(
        prof.key_averages().table(
            sort_by=sort_key,
            row_limit=40,
        )
    )

    print(f"\nTensorBoard log dir: {log_dir}")
    print(f"Run: tensorboard --logdir {log_dir}")


if __name__ == "__main__":
    run_profile()