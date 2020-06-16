# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if start <= end: # make sure the start of the input does not pass the end. If start equals end, means the array has been traversed and the target value was not found.
        mid = (start + end) //2 # get the mid value by adding the start and end and floor dividing them

        if arr[mid] == target: # if target is in the array, it will be returned here after each array is divided down, target should become mid value
            return mid
        elif arr[mid] > target: #target is less than mid point, it will omit the greater values and focus on the left half of the array. This will continue recursively until the value is found
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end) # same for this one, but instead, it will omit the first, lesser half and focus on the greater half of the array. It will recursively split the array until the target is found or values to split run out
    else:
        return -1 #if array is split down and no target value found, it will return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
