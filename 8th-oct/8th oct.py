#Merging 2 sorted lists
def Merlst(lst1, lst2):
    lst1.sort()
    lst2.sort()
    i, j = 0, 0
    merglst = [0]
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merglst.append(lst1[i])
            i = i+1
        else:
            merglst.append(lst2[j])
            j = j+1

    while i < len(lst1):
        merglst.append(lst1[i])
        i = i + 1
    while j < len(lst2):
        merglst.append(lst2[j])
        j += 1
    
    return merglst

lst1 = [9,9,5,9,2]
lst2 = [6,5,1,9,8]
merged_list = Merlst(lst1,lst2)
print(merged_list)
