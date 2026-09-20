Assignment 4
Theory
1. Arrays
An array is a collection of elements of the same data type stored at contiguous memory locations, accessed using an index. In Python, arrays can be represented using lists (built-in) or the NumPy library. For example, [1, 2, 3] is a simple one-dimensional array, and a list of lists like [[1,2],[3,4]] represents a two-dimensional array (matrix).
2. NumPy
NumPy (Numerical Python) is a Python library used for working with arrays. It provides the ndarray object, which supports fast mathematical operations on large sets of numeric data. It is widely used in scientific computing, data analysis, and machine learning.
3. Advantages of NumPy over Python List
NumPy arrays consume less memory compared to lists.
NumPy operations are faster due to internal implementation in C.
NumPy supports vectorized operations (element-wise operations without explicit loops).
NumPy provides many built-in mathematical functions for arrays and matrices.
Lists do not support direct matrix operations like addition, multiplication, etc., whereas NumPy does.

FAQs
1. What is a matrix? How can it be represented in Python using arrays or lists?
A matrix is a rectangular arrangement of numbers into rows and columns. In Python, it can be represented as a list of lists (each inner list being a row) or as a two-dimensional NumPy array.
2. What is the condition for two matrices to be added?
Two matrices can be added only if they have the same order, i.e., the same number of rows and the same number of columns.
3. How do you access individual elements of a 2D array (matrix) in Python?
Individual elements are accessed using two indices, representing the row and column position, e.g., matrix[i][j] for a list of lists or array[i, j] for a NumPy array.
4. Write the general logic or steps to add two matrices element-wise in Python.
Traverse both matrices using nested loops (or use NumPy's + operator), and add the elements present at the same row and column index in both matrices to form the corresponding element of the resultant matrix.
