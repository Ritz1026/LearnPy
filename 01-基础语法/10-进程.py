import multiprocessing
import time


def print_hello():
    time.sleep(2)
    print("Hello from process", multiprocessing.current_process().name)


def print_world():
    time.sleep(2)
    print("World from process", multiprocessing.current_process().name)


"""
需要注意的是，我们在程序的入口处添加了一个条件语句 if __name__ == '__main__':。
这是因为在 Windows 平台上，必须在主程序的入口处添加这个条件语句，以避免多进程运行时出现异常。
在 Linux 和 macOS 等其他操作系统上，这个条件语句是可选的。
"""
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=print_hello)
    process2 = multiprocessing.Process(target=print_world)
    process1.start()
    process2.start()
    # process1.join()
    # process2.join()
    print('Done!')
