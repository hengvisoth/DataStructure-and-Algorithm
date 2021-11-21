def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # arr[1]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1  # i=1  j=1-1=0 a[0] & a[1]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # swap
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [2, 10, 9, 6, 5, 1, 4, 3]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
