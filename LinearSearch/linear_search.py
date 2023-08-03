def linear_search(arr, item):
    for index, element in enumerate(arr):
        if element == item:
            return index
    return None
