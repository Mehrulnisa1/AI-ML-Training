import time


def program_one():
    print("Program 1 running")
    time.sleep(1)


def program_two():
    print("Program 2 running")
    time.sleep(1)


program_one()
program_two()


#Pool + Thread Pool + Process Pool + pool.map()
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]


# Process Pool
with Pool(2) as pool:
    print("Process Pool:", pool.map(square, numbers))


# Thread Pool
with ThreadPool(2) as pool:
    print("Thread Pool:", pool.map(square, numbers))