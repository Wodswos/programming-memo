import asyncio
import threading
import time

# 定义一个简单的任务
def task():
    # pass  # 空任务，或者 time.sleep(0) 来模拟 I/O 等待
    time.sleep(0.1)

# 协程版本
async def async_task():
    # await asyncio.sleep(0)  # 模拟 I/O 等待
    await asyncio.sleep(0.1)

async def run_coroutines(n):
    tasks = [async_task() for _ in range(n)]
    await asyncio.gather(*tasks)

# 线程版本
def thread_task():
    task()

def run_threads(n):
    threads = [threading.Thread(target=thread_task) for _ in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

# 测量执行时间
def measure_time(func, *args):
    start = time.time()
    if asyncio.iscoroutinefunction(func):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(func(*args))
    else:
        func(*args)
    end = time.time()
    return end - start

# 主函数
def main():
    n = 10000  # 任务数量

    # 测量协程执行时间
    coro_time = measure_time(run_coroutines, n)
    print(f"协程执行时间: {coro_time:.6f} 秒")

    # 测量线程执行时间
    thread_time = measure_time(run_threads, n)
    print(f"线程执行时间: {thread_time:.6f} 秒")

if __name__ == "__main__":
    main()