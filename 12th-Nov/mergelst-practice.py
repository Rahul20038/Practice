#merge_sorted_array
def merge_sorted(nums1, nums2, m, n):
    nums2.sort()

    x,y = m-1, n-1
    for z in range(m+n-1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1
    return nums1

nums1 = [2,3,6,0,0,0]
m = 3
nums2 = [9,6,8]
n = 3
merge_array = merge_sorted(nums1, nums2, m, n)
print(merge_array)