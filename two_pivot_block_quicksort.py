import sys
import os
import time

BLOCK_SIZE = 64

def two_pivot_block_partitioning(arr, low, high):
    if low < high:
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        
        # Menentukan dua pivot
        n = high-low+1
        pivot_l, pivot_h = arr[low], arr[high]
        block = [0 for _ in range(BLOCK_SIZE)]

        i, j, k = low + 1, low + 1, 1
        number_p, number_q = 0, 0

        while k < n-1:
            t = min(BLOCK_SIZE, n - k - 1)
            for c in range(t):
                block[number_q] = c
                number_q = number_q + (pivot_h >= arr[k + c + low])

            for c in range(number_q):
                arr[j + c], arr[k + block[c] + low] = arr[k + block[c] + low], arr[j + c]

            k = k + t
            for c in range(number_q):
                block[number_p] = c
                number_p = number_p + (pivot_l > arr[j + c])

            for c in range(number_p):
                arr[i], arr[j + block[c]] = arr[j + block[c]], arr[i]
                i += 1
            
            j += number_q
            number_p, number_q = 0, 0
        
        arr[i-1], arr[low] = arr[low], arr[i-1]
        arr[j], arr[high] = arr[high], arr[j]
        
        return (i-1,j)

def two_pivot_block_quicksort(arr, low = None, high = None):
    if low is None:
        low, high = 0, len(arr)-1
    
    stack = [(low, high)]

    while len(stack):
        l, h = stack.pop()
        i, j = two_pivot_block_partitioning(arr, l, h)

        if l < i-1:
            stack.append((l, i-1))
        if i+1 < j-1:
            stack.append((i+1, j-1))
        if j+1 < h:
            stack.append((j+1, h))
    
    return arr

# def main():

#     sys.setrecursionlimit(2**17)
#     with open(os.path.join('dataset', 'Besar_sorted.txt'), 'r') as file:
#         arr = [num for num in file.read().split('\n')]
#     # print(two_pivot_block_lomuto(test, 1, 2))
#     # arr = [24, 8, 42, 75, 29, 77, 38, 57]
#     #print(two_pivot_block_quicksort(test))
#     start_time = time.time()
#     sorted_arr = two_pivot_block_quicksort(arr)
#     end_time = time.time()
#     print(end_time-start_time)
#     assert sorted(arr) == sorted_arr
# if __name__ == "__main__":
#     main()
