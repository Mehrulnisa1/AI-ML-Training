import time


def cpu_bound():
    total = 0

    for i in range(10_000_000):
        total += i

    return total


def io_bound():
    time.sleep(2)


start = time.time()
cpu_bound()
print("CPU-bound:", time.time() - start)

start = time.time()
io_bound()
print("I/O-bound:", time.time() - start)