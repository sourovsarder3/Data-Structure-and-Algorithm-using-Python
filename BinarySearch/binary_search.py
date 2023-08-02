def binary_search(sorted_list, item):
    start = 0
    end = len(sorted_list)-1
    while start <= end:
        mid = (start+end)//2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            end = mid - 1
        elif guess < item:
            start = mid + 1
    return None
