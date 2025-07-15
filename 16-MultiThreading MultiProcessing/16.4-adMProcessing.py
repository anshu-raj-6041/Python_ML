# MultiProcessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def sq_no(number):
    time.sleep(1)
    return f"Square: {number * number}"


numbers = [1, 2, 3, 4, 5]
if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sq_no, numbers)

    for result in results:
        print(result)



