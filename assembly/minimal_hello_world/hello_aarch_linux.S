// inpsired by JYY os course, write by gemini

// Define system call numbers for AArch64
#define SYS_write 64
#define SYS_exit 93

.globl _start

_start:
    // syscall write(fd, buf, count)
    // fd (stdout) = 1 -> x0
    // buf (address of string) -> x1
    // count (length of string) -> x2
    // syscall number (SYS_write) -> x8

    mov x0, #1              // stdout file descriptor
    ldr x1, =message        // load address of message into x1
    ldr x2, =message_end    // load address of message_end into x2
    sub x2, x2, x1          // calculate length of message (message_end - message)
    mov x8, #SYS_write      // load write system call number into x8
    svc #0                  // make the system call

    // syscall exit(status)
    // status = 100 -> x0
    // syscall number (SYS_exit) -> x8

    mov x0, #100            // exit status
    mov x8, #SYS_exit       // load exit system call number into x8
    svc #0                  // make the system call

.data
message:
    .ascii "\033[01;31mHello, OS World\033[0m\n" // Added \033[0m to reset color
message_end:
    .equ message_len, message_end - message