def binary_search(data, key, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        value = data[mid][key]

        if str(value).lower() == str(target).lower():
            return data[mid]
        elif str(value).lower() < str(target).lower():
            low = mid + 1
        else:
            high = mid - 1

    return None
