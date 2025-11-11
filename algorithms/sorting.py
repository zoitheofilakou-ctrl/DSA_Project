""" 
Contains 3 basic sorting algorithms:
1. Bubble Sort
2. Insertion Sort
3. Merge Sort
"""

def bubble_sort(grades):
# ---------------------------------Bubble short------------------------------------------
# 1. Bubble short(sets the grades of students in ascending order)
#    Each pass compares adjacent grades and swaps them if they are out of the desired order

    l = len(grades) #total number

# runs (n-1) times- after each pass each element is placed to its correct position
    for i in range(l-1):

        #(n-i-1) to ensure we don't recheck the sorted part
        for j in range(0, l-i-1):

            #compare to consequent grades on the list
            if grades[j] > grades[j+1]:
                
                #Swap
                grades[j], grades[j+1] = grades[j+1], grades[j]

                print("Swapped:", grades)

    return grades



# ------------------------------------Insertion Sort -------------------------------

# Phone gallery: each time we download a photo it needs to appear in the right chronological position

def insertion_sort(arr):
    for i in range(1, len(arr)):  # start from the 2nd element
        key = arr[i]
        j = i - 1

        # Move elements greater than the key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        print("Inserted:", arr)
    return arr


# --------------------------Merge Sort--------------------------------

#  Sorting music albums in a playlist with their release years
# from oldest to newest -chronological order

# split the playlist in smaller parts
# sort each part
# merge them back together


def merge_sort(arr):
    # Divide and conquer strategy
    # 1. Divide into 2 halves
    # 2. Recursively sort each half
    # Merge 2 sorted halves into one sorted list

    if len(arr) > 1 : #continue if the list has more than one element

        mid = len(arr)//2  #find middle index
        left_half = arr[:mid] #before midpoint
        right_half = arr[mid:] #after midpoint

        # call recursively merge sort on both halves
        #divides until we reach single elements
        merge_sort(left_half)
        merge_sort(right_half)

        # initialize pointers
        i = j= k = 0 #left (i), right (j), and main list (k)

        # while still remaining elements merge 2 halves
        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]: #compare smallest from each half
                arr[k] = left_half[i] #place the smallest to the main
                i +=1 #move pointer in the left half
            else:
                arr[k] = right_half[j]
                j +=1
            k +=1

        #if any elements left in left half copy them
        while i < len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1


        # If any elements are left in right_half, copy them
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return arr

# -------------------------------
# Testing  sorting algorithms
# -------------------------------

# Bubble Sort example
print("\n==============================")
print("BUBBLE SORT – Sorting Grades")
print("==============================")

student_grades = [56, 87, 93, 45, 58, 76, 38]
print("Grades before sorting:", student_grades)
sorted_grades = bubble_sort(student_grades)
print("Grades after sorting:", sorted_grades)


# Insertion Sort example
print("\n==============================")
print("INSERTION SORT - Organizing Photos by Date")
print("==============================")

photo_dates = [5, 8, 3, 10, 6]  # smaller number = older photo
print("Photo dates before sorting:", photo_dates)
sorted_photos = insertion_sort(photo_dates)
print("Photo dates after sorting:", sorted_photos)



# Merge Sort example

print("\n==============================")
print("Merge SORT - Organizing songs by Date")
print("==============================")
songs = [
    ("Thriller", 1982),
    ("Back in Black", 1980),
    ("Hybrid Theory", 2000),
    ("Nevermind", 1991),
    ("The Eminem Show", 2002),
    ("21", 2011),
]

# Extract release years for sorting
release_years = []
for song in songs:
    release_years.append(song[1])

print("Before sorting:", release_years)
sorted_years = merge_sort(release_years)
print("After sorting:", sorted_years)
