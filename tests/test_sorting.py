from algorithms.sorting import bubble_sort, insertion_sort, merge_sort

print("\n==============================")
print("BUBBLE SORT - Sorting Grades")
print("==============================")
student_grades = [56, 87, 93, 45, 58, 76, 38]
print("Before:", student_grades)
print("After :", bubble_sort(student_grades))


print("\n==============================")
print("INSERTION SORT - Organizing Photos by Date")
print("==============================")
photo_dates = [5, 8, 3, 10, 6]
print("Before:", photo_dates)
print("After :", insertion_sort(photo_dates))


print("\n==============================")
print("MERGE SORT – Organizing Songs by Year")
print("==============================")
songs = [
    ("Thriller", 1982),
    ("Back in Black", 1980),
    ("Hybrid Theory", 2000),
    ("Nevermind", 1991),
    ("The Eminem Show", 2002),
    ("21", 2011),
]
release_years = [song[1] for song in songs]
print("Before:", release_years)
print("After :", merge_sort(release_years))
