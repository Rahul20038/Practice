def oddeven(nums):
    even_count = []
    odd_count = []
    for num in nums:
        if num %2 == 0:
            even_count.append(num)
        else:
            odd_count.append(num)
    even_count.sort()
    odd_count.sort()
    smallest_evennum = even_count[0]
    print(smallest_evennum)
    return even_count, odd_count
nums = [2,6,6,7,8,9,10,3,44,6]
print(oddeven(nums))
