import time

def bubble_sort(data, key, reverse=False):
    arr = data.copy()
    n = len(arr)
    start = time.time()

    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j][key] < arr[j + 1][key]) if reverse else (arr[j][key] > arr[j + 1][key]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end = time.time()
    return arr, (end - start) * 1000

def selection_sort(data, key, reverse=False):
    arr = data.copy()
    n = len(arr)
    start = time.time()

    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (arr[j][key] > arr[idx][key]) if reverse else (arr[j][key] < arr[idx][key]):
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    end = time.time()
    return arr, (end - start) * 1000

def insertion_sort(data, key, reverse=False):
    arr = data.copy()
    start = time.time()

    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j][key] < current[key]) if reverse else (arr[j][key] > current[key])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    end = time.time()
    return arr, (end - start) * 1000

def quick_sort(data, key, reverse=False):
    arr = data.copy()
    start = time.time()

    def _quick_sort_inplace(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            _quick_sort_inplace(arr, low, p - 1)
            _quick_sort_inplace(arr, p + 1, high)

    def partition(arr, low, high):
        pivot = arr[high][key]
        i = low
        for j in range(low, high):
            if (arr[j][key] >= pivot) if reverse else (arr[j][key] <= pivot):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    _quick_sort_inplace(arr, 0, len(arr) - 1)
    end = time.time()
    return arr, (end - start) * 1000
