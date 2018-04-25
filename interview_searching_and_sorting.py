# Binary Search
def binary_search(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = int((first + last) / 2)

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 6))


def rec_binary_search(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mid = int(len(arr) / 2)

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid], ele)
            else:
                return rec_binary_search(arr[mid + 1:], ele)

arr = [1, 2, 3, 4, 5]
# print(rec_binary_search(arr, 5))


####
# Bubble Sort
def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        print("This is the n:", n)
        for k in range(n):
            print("This is the k index check:", k)
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp

arr = [5, 3, 2, 1]
bubble_sort(arr)
print(arr)