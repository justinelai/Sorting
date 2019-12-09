def insertion_sort(list):
    for i in range(1, len(list)):
        # copy item at that index into a temp variable
        temp = list[i]
        # iterate to the left until reaching correct .
        # shift items to the right
        j = i
        while j > 0 and temp < list[j-1]:
            list[j] = list[j-1]
            j -= 1
        list[j] = temp
    return list


# TO-DO: Complete the selection_sort() function below 
# How many loops will be needed to complete this algorithm?
    # How do we know how many items should be shifted over to the right?
    # What do we need to do so that we don't overwrite the value we are `inserting`?
  # What, if anything needs to be returned?
"""
  For every index in the collection from 0 to length-2:
    Compare the element at the current index, i, with everything on its right to identify the position of the smallest element
    Swap the element at i with the smallest element
    i++
Algorithm
Start with current index = 0

For all indices EXCEPT the last index:

a. Loop through elements on right-hand-side of current index and find the smallest element

b. Swap the element at current index with the smallest element found in above loop
"""

test = [ 4, 3, 1, 2, 5, 6 ]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j       
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    print(arr)

selection_sort(test)


# TO-DO:  implement the Bubble Sort function below
 # If `elements` is a collection, remember it will be passed by reference, not value

  # We only need to loop through `elements` until we make a pass that leads to 0 swaps. How do we keep track of whether or not any swaps have occurred?
  # Do we always need to loop through all elements?
    # Depending on how our loop was set up, which neighbors should be compared?
    # Can we do swaps in Python without a `temp` variable?

  # What, if anything needs to be returned?

"""
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

"""