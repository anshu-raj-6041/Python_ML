# Multi Processing => Processes that run in parallel
# when to use multiProcessing?
# CPU-Bound Tasks :: Tasks that are heavy on CPU usage (eg. mathematical computation)
# Parallel execution :: Multiple cores of CPU

import multiprocessing
import time

def sq_no():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_no():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":

    # create 2 process
    p1 = multiprocessing.Process(target=sq_no)
    p2 = multiprocessing.Process(target=cube_no)

    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()