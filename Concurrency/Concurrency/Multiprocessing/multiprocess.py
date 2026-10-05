from multiprocessing import Process, Lock


def work(lock, name):
    with lock:
        print(name, "is using the shared resource")


if __name__ == "__main__":
    lock = Lock()

    p1 = Process(target=work, args=(lock, "Process 1"))
    p2 = Process(target=work, args=(lock, "Process 2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    #Process ID + Process Status

    from multiprocessing import Process
import os
import time


def work():
    print("Child PID:", os.getpid())
    time.sleep(2)


if __name__ == "__main__":
    p = Process(target=work)

    print("Before start:", p.is_alive())

    p.start()

    print("After start:", p.is_alive())
    print("Main PID:", os.getpid())

    p.join()

    print("After completion:", p.is_alive())

    #if __name__ == "__main__"
    def hello():
     print("Hello from function")


if __name__ == "__main__":
    hello()

    