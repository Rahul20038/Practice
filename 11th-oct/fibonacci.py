class Fib():
    def __init__ (self, number):
        self.number = number
    
    def fibonacci_num(self):
        fib_seq = [0,1]
        while len(fib_seq) < self.number:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    def fib_reccur(self):
        if self.number <= 0 :
            return[]
        elif self.number == 1:
            return[0]
        elif self.number == 2:
            return[0,1]
        fib_se = fib_reccur(self - 1)
        fib_se.append(fib_se[-1] + fib_se[-2])
        return fib_se
    def fib3(self):
        a,b = 0,1
        fib3 = []
        for i in range(self.number):
            fib3.append(a)
            a,b = b, a+b
        return fib3

fib1 = Fib(10)
print(fib1.fibonacci_num())



