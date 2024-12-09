def find_duplicates(lst):
    duplicates = set([x for x in lst if lst.count(x > 1)])
    return list(duplicates)
print(find_duplicates([1,1,5,6,9,9,7,2,4,0,6,7]))
