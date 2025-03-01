CC = gcc
CFLAGS = -Wall -g

INCLUDES =-I./include

LIB_DIR  = ./lib
LDFLAGS = -L$(LIB_DIR) -lmylib
SHARED_LIB = $(LIB_DIR)/libmylib.so

all: $(SHARED_LIB) main

# generate shared library
$(SHARED_LIB): src/mylib.o
	$(CC) -shared -o $@ $^

src/mylib.o: src/mylib.c
	$(CC) $(CFLAGS) -fPIC -c $< -o $@

main: src/main.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

src/main.o: src/main.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -rf src/*.o lib/*.so main