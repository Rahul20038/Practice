li = [9,9,5,9,2,6,5,1,9,8]
strt = 0
end = len(li) - 1
while strt < end:
    li[strt],li[end] = li[end],li[strt]
    strt +=1
    end -=1
print(li)
