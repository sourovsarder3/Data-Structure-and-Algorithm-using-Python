def binary_search_recursive(sorted_list, item):
    low = 0
    high = len(sorted_list)-1

    def binary_search(data, item, high, low):
        if low <= high:
            mid = (low + high)//2
            if data[mid] == item:
                return mid
            elif data[mid] > item:
                return binary_search(data, item, mid-1, low)
            else:
                return binary_search(data, item, high, mid+1)
        return None

    return binary_search(sorted_list, item, high, low)
