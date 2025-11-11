# -------------------------------Linear Secrch ------------------------------

def linear_search(arr, target):

# linear search for unsorted movie list
# checks each element one by one
# returns the index if found, otherwise -1
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"found {target} at position {i}")
            return i
    print(f"{target} not found")
    return -1


# ----------------------------- Binary Search ----------------------------------------

def binary_search(arr, target):

# searches for a target value in a sorted list 
# by repeatedly dividing the search interval in half
# returns the index if target is found , otherwise -1

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]


        # checks if x is åresent at mid
        if guess == target:
            print(f"Found '{target}' at position {mid}")
            return mid
        
        # if x is greater ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # if x is smaller ignore right half
        else:
            high = mid - 1

    #if we reach here the element was not present
    print(f"'{target}' not found.")
    return -1