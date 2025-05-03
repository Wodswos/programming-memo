import os
import string

def generate_readable_file(filename, size_mb):
    charset = string.ascii_letters + string.digits + '!@#$%^&*()_+-='
    chunk_size = 1024 * 1024  # 每次写入 1MB
    total_size = size_mb * 1024 * 1024

    with open(filename, 'w') as f:
        while total_size > 0:
            data = ''.join(os.urandom(chunk_size).decode('latin1', 'ignore'))
            filtered = ''.join(c for c in data if c in charset)
            f.write(filtered)
            total_size -= len(filtered)

if __name__ == '__main__':
    generate_readable_file('large_file.txt', 4)  # 生成 4 MB 文件