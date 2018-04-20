# Linear Search
# O(n)
def linear_search(key, li):
    for i, num in enumerate(li):
        if key == num:
            print("{} is found input[{}]".format(key, i))
            break
    else:
        print("{} is not found".format(key))

li = [3, 4, 5, 6, 7, 8, 9, 10, 11]
linear_search(5, li)
linear_search(15, li)

# Binary Search
# O(log n)
def binary_search(key, li):
    find_flag = False
    search_left = 0
    search_right = len(li) - 1

    while search_left < search_right:
        pivot = int((search_left + search_right) / 2)

        if key == li[pivot]:
            find_flag = True
            break
        elif pivot == search_right or pivot == search_left:
            break
        elif key < li[pivot]:
            search_right = pivot
        elif key > li[pivot]:
            search_left = pivot

    if find_flag:
        print("{} is found input[{}]".format(key, pivot))
    else:
        print("{} is not found".format(key))

li = [3, 4, 5, 6, 7, 8, 9, 10, 11]
binary_search(9, li)
binary_search(12, li)

# Bubble Sort
# O(n^2)
def bubble_sort(li):
    for i in range(0, len(li) - 1):
        for j in range(1, len(li) - i):
            if li[j - 1] > li[j]:
                li[j], li[j - 1] = li[j - 1], li[j]

li = [12, 3, 4, 5, 10, 7, 8, 9, 11]
bubble_sort(li)
print(li)

# Selection Sort
# O(n^2)
def selection_sort(li):
    for i in range(0, len(li)):
        min_i = i
        for j in range(i + 1, len(li)):
            if li[min_i] > li[j]:
                min_i = j
        li[min_i], li[i] = li[i], li[min_i]

li = [12, 3, 4, 5, 10, 7, 8, 9, 11]
selection_sort(li)
print(li)

# Insertion Sort
# O(n^2)
def insertion_sort(li):
    for i in range(1, len(li)):
        select = li[i]
        if li[i - 1] > select:
            j = i
            li[j] = li[j - 1]
            j -= 1
            while j > 0 and li[j - 1] > select:
                li[j] = li[j - 1]
                j -= 1
            li[j] = select

li = [12, 3, 4, 5, 10, 7, 8, 9, 11]
insertion_sort(li)
print(li)

# Merge Sort
# O(n log n)
def merge_sort(li):
    def _merge(data1, data2):
        result = []
        item1 = data1[0]
        item2 = data2[0]

        while(True):
            if item1 < item2:
                result.append(data1.pop(0))
                if len(data1) == 0:
                    result.extend(data2)
                    break
                item1 = data1[0]
            else:
                result.append(data2.pop(0))
                if len(data2) == 0:
                    result.extend(data1)
                    break
                item2 = data2[0]
        return result

    def _split(li):
        length = len(li)
        data1 = li[0:int(length / 2)]
        data2 = li[int(length / 2):length]
        return data1, data2

    def _merge_sort(li):
        if len(li) <= 1:
            return li
        data1, data2 = _split(li)
        return _merge(_merge_sort(data1), _merge_sort(data2))

    return _merge_sort(li)

li = [12, 3, 4, 5, 10, 7, 8, 9, 11]
li = merge_sort(li)
print(li)

# Quick Sort
# O(n log n)
def quick_sort(li):
    def _quick_sort(li):
        if len(li) == 0:
            return li
        pivot = li[0]
        left = []
        right = []

        for i in range(1, len(li)):
            if li[i] <= pivot:
                left.append(li[i])
            else:
                right.append(li[i])
        left = _quick_sort(left)
        right = _quick_sort(right)
        return left + [pivot] + right

    return _quick_sort(li)

li = [12, 3, 4, 5, 10, 7, 8, 9, 11]
li = quick_sort(li)
print(li)

# Heap Sort
# O(n log n)
def left(i):
    return int(i * 2 + 1)

def right(i):
    return int(i * 2 * 2)

def parent(i):
    return int((i - 1) / 2)

def heapify(li):
    last = int((len(li) - 1) / 2)
    
    for i in range(last, 0, -1):
        while True:
            if left(i) < len(li) and li[i] > li[left(i)]:
                li[i], li[left(i)] = li[left(i)], li[i]
            if right(i) < len(li) and li[i] > li[right(i)]:
                li[i], li[right(i)] = li[right(i)], li[i]
            if i == 0:
                break
            i = parent(i)
    return li

def heap_sort(li):
    result = []
    li = heapify(li)
    for i in range(len(li)):
        result.append(li.pop(0))
    return result

li = [12, 3, 4, 5, 10, 7, 8, 9, 11]
li = heap_sort(li)
print(li)
