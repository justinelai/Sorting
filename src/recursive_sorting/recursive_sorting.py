## FROM GUIDED PROJECT: QUICKSORT
def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    
    return left, [pivot], right

def quicksort(data)
    if len(data) <= 1:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + pivot + quicksort(right)
    #return concatenation


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
