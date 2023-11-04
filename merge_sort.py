def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    final = []
    pointer1, pointer2 = 0, 0
    while pointer1 < len(left) and pointer2 < len(right):
        if left[pointer1] < right[pointer2]:
            final.append(left[pointer1])
            pointer1 += 1
        else:
            final.append(right[pointer2])
            pointer2 += 1

    while pointer1 < len(left):
        final.append(left[pointer1])
        pointer1 += 1

    while pointer2 < len(right):
        final.append(right[pointer2])
        pointer2  += 1
    
    return final


if __name__ == '__main__':
    arr = [24, 8, 42, 75, 29, 77, 38, 57]
    assert sorted(arr) == merge_sort(arr)
    