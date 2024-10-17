#factorialnum
def factnum(n):
    factorial = 1
    if n < 0:
        print("sorry negative num cannot exsist")
    elif n == 0:
        print("factorial of zero is 1")
    else:
        for i in range(1, n+1):
            factorial = factorial * i
        print(f"the factorial of {n} is {factorial}")
factnum(int(input("enter your num")))
           