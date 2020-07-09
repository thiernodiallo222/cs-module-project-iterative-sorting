def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i+=1
    return -1 

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    found = False 
    while (start <= end):
        mid = (start+end)//2
        if (target > arr[mid]):
            start = mid + 1
        elif (target < arr[mid]):
            end = mid - 1
        else:
            return mid 
    return -1  # not found

    # this is a comment
