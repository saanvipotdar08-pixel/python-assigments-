student = {"name": "Raj", "age": 20, "course": "Python"}
print("Original Dictionary:", student)

student["grade"] = "A"
print("After Adding a key-value pair:", student)

student["age"] = 21
print("After Updating age:", student)

del student["grade"]
print("After Deleting 'grade':", student)

removed_value = student.pop("course")
print("Removed value using pop():", removed_value)
print("Dictionary after pop():", student)


fruits = ("apple", "banana", "cherry")
print("Original Tuple:", fruits)

fruits = fruits + ("mango",)
print("After Adding an item (concatenation):", fruits)

temp_list = list(fruits)
temp_list.remove("banana")
fruits = tuple(temp_list)
print("After Removing an item:", fruits)

print("Count of 'apple':", fruits.count("apple"))
print("Index of 'cherry':", fruits.index("cherry"))