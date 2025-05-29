ifeq ($(shell uname -s), Darwin)
    CC = clang
    FRAMEWORKS = -framework Foundation
    CFLAGS += -fobjc-arc
else
    CC = gcc
endif

CFLAGS = -std=c11 -Wall -Wextra


test_enum: enum.c
	$(CC) $(CFLAGS) -o test_enum $^
	./test_enum
	rm -f test_enum

test_pipe: pipe.c
	$(CC) -o test_pipe $^
	./test_pipe
	rm -f test_pipe

test_spawn: posix_spawn.c
	$(CC) -o test_spawn $^
	./test_spawn
	rm -f test_spawn

clean:
	rm -f test_enum
