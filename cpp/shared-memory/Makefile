ifeq ($(shell uname -s), Darwin)
    CC = clang++
else
    CC = g++
	CFLAGS = -lrt
endif

# clang++ or clang -lc++

test_shmem: writer.cc reader.cc
	$(CC) $(CFLAGS) -o writer writer.cc
	$(CC) $(CFLAGS) -o reader reader.cc

clean:
	rm -f writer reader
