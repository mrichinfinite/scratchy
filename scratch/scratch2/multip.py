# Multiprocessing and threading
# For more information see here: https://www.python-engineer.com/courses/advancedpython/15-thread-vs-process/

# Multiprocessing
from multiprocessing import Process, process
import os
import time

# The function that the process will execute.
def square_numbers():
    for i in range (100):
        i * i
        time.sleep(0.1)

processes = []
# Get CPU count from local machine.
num_processes = os.cpu_count()

# Create processes.
for i in range(num_processes):
    '''p equals a new process. Target here is previously defined function above. 
    Must specify "args" argument if there is an argument in the previously defined function above.'''
    p = Process(target=square_numbers)
    processes.append(p)

# Start each process.
for p in processes:
    p.start()

# Join processes.
for p in process:
    # What for process(es) to finish, and while you are waiting, block the main thread.
    p.join()

# You will reach this point when all processes are done.
print('end main')

# Threading
from threading import Thread

def square_numbers():
    for i in range (100):
        i * i
        time.sleep(0.1)

threads = []
# Number of threads in process.
num_threads = 10

# Create threads.
for i in range(num_threads):
    '''t equals a new thread. Target here is previously defined function above. 
    Must specify "args" argument if there is an argument in the previously defined function above.'''
    t = Thread(target=square_numbers)
    threads.append(t)

# Start each thread.
for t in threads:
    t.start()

# Join threads.
for t in threads:
    t.join()

print('end main')

# Watch Task Manager or Activity Monitor on local machine to see the result.