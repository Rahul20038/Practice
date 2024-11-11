#merge sorted array in leetcode
def merge_sorted_array(nums1, nums2, m, n):
    x,y = m-1, n-1
    for z in range(m+n-1,-1,-1):
        if x < 0:
            nums1[z] = nums2[y]
            y -=1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -=1
        else:
            nums1[z] = nums2[y]
            y -=1
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [1,5,6]
m = 3  #count how many valid elements in nums1
n = 3  #count how many valid elements in nums2
merged_array = merge_sorted_array(nums1, nums2, m, n)
print(merged_array)