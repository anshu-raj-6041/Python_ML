'''
Real-World Ex: MultiProcessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large no, involve significant computational work.
MultiProcessing can be used to distribute the workload across multiple CPU cores, involving the performance.
'''

import multiprocessing
import math
import multiprocessing.pool
import sys
import time

# Increase the max no of digits for integer conversion
sys.set_int_max_str_digits(100000)

# fn to compute factorial of a given number
def compute_fac(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]
    start_time = time.time()

    # create a pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_fac, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")