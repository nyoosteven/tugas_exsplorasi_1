from two_pivot_block_quicksort import two_pivot_block_quicksort,two_pivot_block_partitioning
from memory_profiler import memory_usage
import sys
import os
import time

def profile_sort(sort_function, arr):
    memory_usages = memory_usage((time_profile_sort, (sort_function, arr)), max_iterations=1)
    print(f'{max(memory_usages)} MB')

def time_profile_sort(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    print(f'{(end_time - start_time) * 1000} ms')

if __name__ == '__main__':
    sys.setrecursionlimit(2**17)
    with open(os.path.join('dataset', 'Besar_sorted.txt'), 'r') as file:
        arr = [num for num in file.read().split('\n')]
        profile_sort(two_pivot_block_quicksort,arr)