cmake_minimum_required(VERSION 3.10)
project(FindDemo)

# 查找 Zlib
find_package(ZLIB REQUIRED)

# 打印所有 Zlib 相关变量
message("== Zlib 信息 ==")
message("  是否找到: ${ZLIB_FOUND}")
message("  版本: ${ZLIB_VERSION}")
message("  头文件路径: ${ZLIB_INCLUDE_DIRS}")
message("  库文件路径: ${ZLIB_LIBRARIES}")
message("  库文件详细路径: ${ZLIB_LIBRARY}")  # 单个库路径（如 libz.so）

# 创建可执行文件
add_executable(demo main.c)

# 链接 Zlib
target_link_libraries(demo PRIVATE ZLIB::ZLIB)