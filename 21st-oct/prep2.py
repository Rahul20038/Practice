#inverted Pyramid
def inverted_pyr(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()
n = 7
print(inverted_pyr(n))