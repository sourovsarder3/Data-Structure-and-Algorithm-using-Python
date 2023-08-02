def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list)-1
    while low <= high:
        mid = (low+high)//2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None
