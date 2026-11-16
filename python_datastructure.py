# ==========================================
# 1. List Rotation (Left/Right by k positions)
# ==========================================
print("--- 1. List Rotation ---")
lst = [1, 2, 3, 4, 5]
print("Original List:", lst)
k = int(input("Enter positions to rotate: "))
direction = input("Enter direction (left/right): ").lower()

n = len(lst)
k = k % n  # Handle if k is greater than list length

if direction == "left":
    rotated = lst[k:] + lst[:k]
elif direction == "right":
    rotated = lst[n-k:] + lst[:n-k]
else:
    rotated = lst

print("Rotated List:", rotated)


# ==========================================
# 2. Remove Duplicates Without Using Set
# ==========================================
print("\n--- 2. Remove Duplicates without Set ---")
lst = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original List:", lst)
unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print("List after removing duplicates:", unique_lst)


# ==========================================
# 3. Find Missing Number (1 to n)
# ==========================================
print("\n--- 3. Find Missing Number ---")
# Example: numbers from 1 to 5 with one missing
arr = [1, 2, 4, 5]  # Here 3 is missing
n = 5  # Total numbers should be from 1 to 5

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum

print("List:", arr)
print("Missing Number is:", missing)


# ==========================================
# 4. Tuple Operations (5 Subjects)
# ==========================================
print("\n--- 4. Tuple Operations ---")
subjects = ("Math", "Physics", "Chemistry", "Python", "English")

print("Subjects Tuple:", subjects)
print("Third subject:", subjects[2])
print("Total subjects:", len(subjects))
print("Index of 'Python':", subjects.index("Python"))


# ==========================================
# 5. Convert Tuple to Dictionary
# ==========================================
print("\n--- 5. Convert Tuple to Dictionary ---")
tuple_data = ((1, "A"), (2, "B"), (3, "C"))
print("Original Tuple:", tuple_data)

result_dict = {}
for item in tuple_data:
    result_dict[item[0]] = item[1]

print("Converted Dictionary:", result_dict)


# ==========================================
# 6. Tuple Unpacking Logic (Swap First & Last)
# ==========================================
print("\n--- 6. Swap First and Last Elements in Tuple ---")
tup = (10, 20, 30, 40, 50)
print("Original Tuple:", tup)

# Convert to list temporarily just to swap, or use tuple packing/unpacking
lst_tup = list(tup)
lst_tup[0], lst_tup[-1] = lst_tup[-1], lst_tup[0]
tup = tuple(lst_tup)

print("Tuple after swapping first and last:", tup)


# ==========================================
# 7. Subset Checker
# ==========================================
print("\n--- 7. Subset Checker ---")
set1 = {2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is a subset of set2 without using .issubset() directly if needed, or using it simply:
is_subset = True
for item in set1:
    if item not in set2:
        is_subset = False
        break

print("Set 1:", set1)
print("Set 2:", set2)
if is_subset:
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is NOT a subset of Set 2")


# ==========================================
# 8. Student Marks Analyzer
# ==========================================
print("\n--- 8. Student Marks Analyzer ---")
students = {
    "Rahul": 75,
    "Amit": 28,
    "Priya": 92,
    "Neha": 45,
    "Rohit": 30
}

total_marks = 0
failures = []
topper = ""
max_marks = -1

for name, marks in students.items():
    total_marks += marks
    if marks < 33:
        failures.append(name)
    if marks > max_marks:
        max_marks = marks
        topper = name

average = total_marks / len(students)

print("Students & Marks:", students)
print("Topper:", topper, "with", max_marks, "marks")
print("Average Marks:", average)
print("Failed Students (< 33):", failures)


# ==========================================
# 9. Library Management Using Dictionary
# ==========================================
print("\n--- 9. Library Management ---")
library = {
    "Python Programming": 5,
    "Data Structures": 3,
    "Computer Networks": 4
}

print("Initial Library Stock:", library)

# Add a new book or update quantity
book_name = "Digital Electronics"
quantity = 6
library[book_name] = quantity

print("Updated Library Stock:", library)