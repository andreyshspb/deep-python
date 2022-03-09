import multiprocessing
import time
from datetime import datetime
from multiprocessing import Queue
import codecs


def first_function(main_to_first: Queue, first_to_second: Queue):
    while True:
        time.sleep(5)
        while not main_to_first.empty():
            data = main_to_first.get_nowait().lower()
            first_to_second.put(data)


def second_function(first_to_second: Queue, second_to_main: Queue):
    while True:
        data = codecs.encode(first_to_second.get(), 'rot_13')
        second_to_main.put(data)


def main():
    main_to_first = Queue()
    first_to_second = Queue()
    second_to_main = Queue()

    multiprocessing.Process(target=first_function, args=(main_to_first, first_to_second), daemon=True).start()
    multiprocessing.Process(target=second_function, args=(first_to_second, second_to_main), daemon=True).start()

    while True:
        message = input(datetime.now().strftime('%H:%M:%S') + '> ')
        main_to_first.put(message)
        result = second_to_main.get()
        print(datetime.now().strftime('%H:%M:%S') + '>', result)


if __name__ == '__main__':
    main()
