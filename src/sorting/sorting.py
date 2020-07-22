# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # I don't know what the array above does so I made a new one
    result = []
    # Starting index for comparison
    left_index, right_index = 0, 0
    # Then compares each item in the array at each index
    while left_index < len(arrA) and right_index < len(arrB):
        # Compares if the left is less than the right
        # then adds it to the result array and then compares the next index
        if arrA[left_index] < arrB[right_index]:
            result.append(arrA[left_index])
            left_index += 1
        else:
            # Same as the above but for the right side
            result.append(arrB[right_index])
            right_index += 1
   # then continuosly adds the arrays to the resulting array         
    result += arrA[left_index:]
    result += arrB[right_index:]

    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # and if the length of the array is less than or equal to 1 return the array
    if len(arr) <= 1:
        return arr
    # take the array and split it in half
    else:
        half = len(arr) // 2
    # split the array in half untill the length is zero
        upper_half = merge_sort(arr[half:])
        lower_half = merge_sort(arr[:half])
    
    return merge(upper_half,lower_half)

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

