# .S need preprocess

aarch_linux:
	gcc -E hello_aarch_linux.S # or cpp hello_aarch_linux.S
	as -o hello.o hello.s
	ld hello hello.o
	./hello


aarch_macos:
	as -arch arm64 -o hello.o hello_aarch_mac.s
	ld -o hello hello.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _main -arch arm64
	./hello

clean:
	rm -f hello hello.o hello.s