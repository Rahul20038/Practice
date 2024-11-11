#merge sorted array in leetcode
nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]
m = 3
n = 3
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
