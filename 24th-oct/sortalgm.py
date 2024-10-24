#Sorting algorthim
lst = [7,8,5,2,9,8,8,1,8]
print(lst)
for i in range(len(lst)):
    min_val = min(lst[i:])
    min_inx = lst.index(min_val)
    lst[i], lst[min_inx] = lst[min_inx], lst[i]

print(lst)