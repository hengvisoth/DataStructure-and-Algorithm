import array as arr
a = arr.array('i',[2,4,6,8])
#1
print("First Element : ",a[0])
print("Last Element : ",a[-1])
#2
a.insert(1,3)
print("After add : ",a)
#3 Delete the element 8
a.remove(8)

#4 Modify the element 6 as 5

a[3] = 5

print("Final Result",a)
