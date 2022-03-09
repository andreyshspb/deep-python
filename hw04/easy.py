import time
from multiprocessing import Process
from threading import Thread


def fib(n: int) -> int:
    assert n > 0
    if n == 1 or n == 2:
        return 1
    temp1, temp2 = 1, 1
    for _ in range(n - 2):
        temp1, temp2 = temp2, temp1 + temp2
    return temp2


def calculate_time(threads) -> float:
    start_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return time.time() - start_time


if __name__ == '__main__':
    n = 100000

    start_time = time.time()
    for _ in range(10):
        fib(n)
    sync_time = time.time() - start_time

    threads = [Thread(target=fib, args=(n,)) for _ in range(10)]
    threads_time = calculate_time(threads)

    processes = [Process(target=fib, args=(n,)) for _ in range(10)]
    process_time = calculate_time(processes)

    with open('artifacts/easy.txt', 'w') as file:
        file.write(f'sync time: {sync_time}s\n')
        file.write(f'threads time: {threads_time}s\n')
        file.write(f'process time: {process_time}s\n')
