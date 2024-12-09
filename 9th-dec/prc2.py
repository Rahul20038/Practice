def find_duplicates(lst):
    duplicates = set([x for x in lst if lst.count(x) > 1])
    return list(duplicates)
print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))