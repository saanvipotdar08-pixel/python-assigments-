Aim:
Write a python program to create, append and remove etc. operation on Dictionary and Tuple. 

Theory:

1.Explain Lists in Python with the help of at least five methods.

A list is a collection of items stored in one variable, written using square brackets []. Lists can hold different types of data and can be changed after creation (mutable). They keep the order of items and allow duplicate values.
Methods:
- append() – adds an item at the end of the list
- insert() – adds an item at a particular position
- remove() – removes a given item from the list
- pop() – removes an item from a position and returns it
- sort() – arranges the items in ascending order


2. Explain Tuples in Python with the help of at least five methods.
A tuple is also a collection of items but it is immutable, meaning once created it cannot be changed. It is written using round brackets (). Tuples maintain order and allow duplicate values, and they are faster than lists.
Methods:
- count() – tells how many times a value appears in the tuple
- index() – gives the position of a value in the tuple
- len() – gives the total number of items in the tuple
- tuple() – converts another data type like a list into a tuple
- slicing – used to get a part of the tuple
Since tuples can't be changed, they don't have methods like append, insert or remove.


3. Explain Dictionaries in Python with the help of at least five methods.
A dictionary stores data in key-value pairs instead of just values. It is written using curly braces {}. Dictionaries are mutable, keys must be unique, and from Python 3.7 they maintain insertion order.

Methods:
- get() – returns the value of a given key
- keys() – returns all the keys in the dictionary
- values() – returns all the values in the dictionary
- items() – returns key-value pairs together
- update() – adds new key-value pairs or updates existing ones


FAQs
**Q1.**
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])

Output: [1, 3, 5, 7, 9]

Explanation: a[::2] takes every second element starting from index 0, so it picks 1, 3, 5, 7, 9.

**Q2.**
l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)

Output: ()

Explanation: l.__len__() is 3, and l[::-1][0] is also 3 (first element of reversed list). So it becomes ('Python',) * 0, which gives an empty tuple ().

**Q3.**
A list is mutable, written in square brackets, and stores an ordered sequence of items that can be changed. A tuple is immutable, written in round brackets, and also stores an ordered sequence but cannot be changed after creation. A dictionary stores data as key-value pairs in curly braces, is mutable, and values are accessed using keys instead of index numbers.

**Q4.**
Tuple assignment lets multiple variables be assigned in one line, making code shorter and cleaner. It allows easy swapping of variable values without a temporary variable, and helps in unpacking values from lists or tuples directly into separate variables.
