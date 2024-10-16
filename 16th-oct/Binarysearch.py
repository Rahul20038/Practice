def binaryser(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return -1
arr = [9,9,5,9,2,6,5,1,9,8]
target = 8
result = binaryser(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")