import random

def generate_dataset(n, lower_limit, upper_limit):
    arr = []
    for _ in range(n):
        arr.append(random.randint(lower_limit, upper_limit))
    return arr

def reverse_dataset(arr):   
    return arr[::-1]

def sorted_dataset(arr):
    return sorted(arr)

def save_to_file(filename, dataset):
    with open(filename, 'w') as file:
        for number in dataset:
            file.write(f"{number}\n")

number = [9,13,16]
ukuran = ['Kecil', 'Sedang', 'Besar']
for i in range(len(number)):
    dataset = generate_dataset(2**number[i], 1, 10**9)
    save_to_file(f"{ukuran[i]}.txt", dataset)

    dataset_reverse = reverse_dataset(dataset)
    save_to_file(f"{ukuran[i]}_reverse.txt", dataset_reverse)
    
    dataset_sorted = sorted_dataset(dataset)
    save_to_file(f"{ukuran[i]}_sorted.txt", dataset_sorted)