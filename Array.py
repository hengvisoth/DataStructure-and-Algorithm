# method 1
import array as arr     # with alias name
a = arr.array("i", [1, 2, 3,3,4])
print(a)
# method 2
import array    # with alias name
a = array.array("i", [1, 2, 3,3,4])
print(a)
#method3

from array import *
number = array('i', [1, 2, 3, 3, 4])
print(number[0],number[1],number[-1])
print(number)
# append
number.append(4)
print(number)
#delete
del number[0]
print(number)
#replace the value
number[1] = 1
print(number)
#extend() : same as append but it can expand more than one value
number.extend([5,6,7])
print(number)
# slicing
print(number[2:5])


import array as arr
number = arr.array('i', [1, 2, 3, 3, 4])
print(number)
x=len(number)
print(x)
for x in number:
    print(x)
# First method to create a 1 D array
N = 5
arr = [0]*N
print(arr)
# Second method to create a 1 D array
N = 5
arr = [0 for i in range(N)]
print(arr)
#Method 1
# 2D array
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)

 #Method2
# 2D array
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)
print(arr[-1],arr[2],arr[0])
#delete the whole array
# del number
# print(number)
