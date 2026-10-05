import time


def task_one():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)


def task_two():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)


task_one()
task_two()

#Process-Based Multitasking + Process
from multiprocessing import Process
import os


def work():
    print("Child Process ID:", os.getpid())


if __name__ == "__main__":
    print("Main Process ID:", os.getpid())

    p = Process(target=work)
    p.start()
    p.join()