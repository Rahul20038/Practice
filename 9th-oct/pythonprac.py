def larsmall(arr):
    if not arr:
        print("array is empty")
    min_element = arr[0]
    max_element = arr[0]
    for i in arr:
        if i < min_element:
            min_element = i
        if i > max_element:
            max_element = i
    return min_element, max_element

arr = [3,4,5,6,2,7,8,9]
smallest, largest = larsmall(arr)
print("smallest number is :",smallest )
print("largest number is :", largest)
