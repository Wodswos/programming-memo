#include <stdio.h>
#include <stdlib.h>
#include <spawn.h>    // posix_spawn 头文件
#include <sys/wait.h>

extern char **environ; // 外部环境变量

int main() {
    pid_t pid;
    char *argv[] = { "ls", "-l", NULL };

    // 1. 定义文件操作（可选）
    posix_spawn_file_actions_t file_actions;
    posix_spawn_file_actions_init(&file_actions);
    // 示例：重定向 stdout 到文件（需手动打开文件）
    // posix_spawn_file_actions_addopen(&file_actions, STDOUT_FILENO, "output.txt", O_WRONLY|O_CREAT, 0644);

    // 2. 定义进程属性（可选）
    posix_spawnattr_t attr;
    posix_spawnattr_init(&attr);
    // 示例：设置信号掩码（继承父进程信号设置）
    // sigset_t sigmask;
    // sigemptyset(&sigmask);
    // posix_spawnattr_setsigmask(&attr, &sigmask);

    // 3. 调用 posix_spawn
    int status = posix_spawnp(
        &pid,                    // 子进程 PID 输出
        "ls",                    // 可执行文件名（自动搜索 PATH）
        &file_actions,           // 文件操作结构体（NULL 表示无操作）
        &attr,                   // 进程属性（NULL 表示默认）
        argv,                    // 命令行参数数组
        environ                  // 环境变量（继承父进程）
    );

    if (status != 0) {
        perror("posix_spawn failed");
        exit(EXIT_FAILURE);
    }

    // 4. 等待子进程结束
    waitpid(pid, &status, 0);

    // 5. 清理资源
    posix_spawn_file_actions_destroy(&file_actions);
    posix_spawnattr_destroy(&attr);

    return 0;
}
