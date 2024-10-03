li = [10,2,5,9,15,56]
#method-1
#li.sort()
#smallest = li[0]
#largest = li[-1]
#print(smallest)
#print(largest)
#method-2
#print("smallest number is",min(li))
#print("largest number is",max(li))
if len(li) == 0:
    print("None")
largest = smallest = li[0]
for i in li:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print(largest,smallest)
