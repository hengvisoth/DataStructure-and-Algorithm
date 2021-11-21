def insertionSort(arr):
    for i in range(0,len(arr)):

        j=i-1
        while arr[i] > arr[j+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            j-=1
        arr[i] = arr[j]
    return arr
print(insertionSort([5,2,54,7,9,3]))
