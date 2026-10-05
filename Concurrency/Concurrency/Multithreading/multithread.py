import threading
import time


def work(name):
    for i in range(3):
        print(name, i)
        time.sleep(1)


t1 = threading.Thread(target=work, args=("Thread 1",))
t2 = threading.Thread(target=work, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed")