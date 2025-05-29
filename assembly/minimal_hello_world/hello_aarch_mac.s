// hello_macos.s
// Assembly program to print "Hello World" and exit on macOS AArch64

.section __DATA,__data
hello_string:
    .asciz "Hello MacOS\n"  // Null-terminated string
string_len = . - hello_string - 1 // Calculate string length (excluding null terminator)

.section __TEXT,__text
.globl _main                // Entry point for the linker
.align 4                    // Align to a 4-byte boundary

_main:
    // --- write(fd, buffer, count) ---
    // fd (file descriptor): x0 = 1 (stdout)
    // buffer (address of string): x1
    // count (string length): x2
    // syscall number for write: x16 (newer macOS) or w8 (older)
    // On modern macOS (roughly 11.0+), syscalls are generally invoked via x16.
    // The specific syscall numbers can sometimes vary slightly or have aliases.
    // For write, it's typically 4.

    mov     x0, #1              // 1 = stdout
    adrp    x1, hello_string@PAGE // Load page address of hello_string
    add     x1, x1, hello_string@PAGEOFF // Add page offset to get full address
    mov     x2, #string_len     // Load length of the string
    mov     x16, #4             // Syscall number for write (unix_write)
    svc     #0                  // Perform the system call

    // --- exit(status) ---
    // status (exit code): x0
    // syscall number for exit: x16 (newer macOS) or w8 (older)
    // For exit, it's typically 1.

    mov     x0, #0              // Exit code 0 (success)
    mov     x16, #1             // Syscall number for exit (unix_exit)
    svc     #0                  // Perform the system call

// No need for a return instruction as exit syscall terminates the process.