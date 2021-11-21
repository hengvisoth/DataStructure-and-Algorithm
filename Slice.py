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
print(arr[:-1],arr[:],arr[0:])
