import torch
from torch.profiler import profile, record_function, ProfilerActivity

device = "cuda" if torch.cuda.is_available() else "cpu"

activities = [ProfilerActivity.CPU]
if device == "cuda":
    activities.append(ProfilerActivity.CUDA)

x = torch.randn(2048, 2048, device=device)
w = torch.randn(2048, 2048, device=device)

with profile(
    activities=activities,
    record_shapes=True,
    with_flops=True,
) as prof:
    with record_function("matmul_relu_block"):
        y = torch.relu(x @ w)

    # y = torch.relu(x @ w)

    if device == "cuda":
        torch.cuda.synchronize()

sort_key = "cuda_time_total" if device == "cuda" else "cpu_time_total"

print(
    prof.key_averages().table(
        sort_by=sort_key,
        row_limit=20
    )
)