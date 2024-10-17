#swappingnumbers
def swapnum(x,y):
    temp = x
    x = y
    y = temp
    return x,y
x = 9
y = 99
x,y = swapnum(x,y)
print(f"x:{x} y:{y}")