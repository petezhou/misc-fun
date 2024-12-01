import sys
import time
from concurrent.futures import ProcessPoolExecutor

def is_prime_single_thread(num: float, start: int, end: int):
    for i in range(start, end):
        if num % i == 0:
            return False
    return True


def is_prime_multi_thread(num: float, num_threads: int, half_way: int):
    with ProcessPoolExecutor(max_workers=num_threads) as executor:
        futures = []

        chunk_size = half_way // num_threads
        start = 2
        for _ in range(num_threads):
            end = start + chunk_size
            futures.append(executor.submit(is_prime_single_thread, num, start, end))
            start = end + 1
        for future in futures:
            if not future.result():
                return False
        return True


if __name__ == "__main__":
    num = float(sys.argv[1])
    num_threads = int(sys.argv[2])
    print(f"Is {int(num)} prime? Calculating with {num_threads} threads.")

    start_time = time.time()
    half_way = int(round(num // 2, 0)) + 1
    if num_threads == 1:
        print(is_prime_single_thread(num, 2, half_way))
    else:
        print(is_prime_multi_thread(num, num_threads, half_way))
    end_time = time.time()
    print(f"Took {round(end_time - start_time, 2)} seconds")
