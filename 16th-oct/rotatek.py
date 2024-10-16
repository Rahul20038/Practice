def rotate_k(arr,k):
    n = len(arr)
    k = k % n
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr
arr = [9,9,5,9,2,6,5,1,9,8]
k = 4
print(rotate_k(arr, k))