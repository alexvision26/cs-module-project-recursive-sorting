# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = [] # resulting merged array
    # Your code here
    # initialize index iterators
    lp = 0 
    rp = 0

    while lp < len(arrA) and rp < len(arrB): # this loop will run until both splits are sorted into the merged_array. compares the incrementor to the actual length of the array. left or right only incremented if appended.
        if arrA[lp] < arrB[rp]: #compares each value between the two arrays
            merged_arr.append(arrA[lp]) # if left value is smaller, it is appended first, then the index is incremented
            lp += 1
        else:
            merged_arr.append(arrB[rp]) # if right value is smaller, it is appended first
            rp += 1

    if lp == len(arrA):
        merged_arr.extend(arrB[rp:]) # adds the rest of the rigth elements onto the merged array if left array were to append all elements first
    else:
        merged_arr.extend(arrA[lp:]) # the inverse, if the right elements are all appended, appends the rest of the left array onto the merged array

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1: #if the array is 1 or less, there is nothing to sort
        return arr
    mid = int(len(arr) / 2) #grabs the mid point of the array

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:]) # recursively splits the array from the mid point. Will take left, and right and split those again due to recursive function call until their lengths are 1 or less

    return merge(left, right) #passes each split into merge helper function which sorts the split back into a merged array

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
