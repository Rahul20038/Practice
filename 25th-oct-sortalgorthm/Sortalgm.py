lst = [5,4,8,9,7,5,4,9,5,5,3,9,7]
print("Unsorted List", lst)
for i in range (len(lst)-1):
    min_val = min(lst[i:])
    min_index = lst.index(min_val, i)
    if lst[i] != lst[min_index] :
        lst[i], lst[min_index] = lst[min_index], lst[i]
    print("Sorted List", lst)