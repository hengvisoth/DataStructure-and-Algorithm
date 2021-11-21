ls = [3,2,5,7,4,9,10]
sorted_ls = []
for i in range(len(ls)):
    sorted_ls.append(min(ls))
    ls.remove(min(ls))

print(sorted_ls)
arr = [86,84,80,88,89,85,86,82,82,79,86,80,82,76,86,89,87,83,80,88,86,81,81,87]
res =0
sq = 0
a=0
for i in arr:
    a+=1
    res+=i
    sq+=i*i
print(res)
print(sq)
print(a)
