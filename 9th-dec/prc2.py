def find_duplicates(lst):
    duplicates = set([x for x in lst if lst.count(x > 1)])
    return list(duplicates)
print(find_duplicates([9,9,5,9,2,6,5,1,9,8,1]))