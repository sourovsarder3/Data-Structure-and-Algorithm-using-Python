def linear_search_recursive(arr, item):

    def linear_search(arr, item, index):

        if index > len(arr)-1:
            return None
        if arr[index] == item:
            return index
        else:
            index += 1
            return linear_search(arr, item, index)
    return linear_search(arr, item, 0)
