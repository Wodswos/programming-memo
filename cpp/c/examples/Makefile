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

clean:
	rm -f test_enum
