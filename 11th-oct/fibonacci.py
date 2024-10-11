class Fib():
    def __init__ (self, number):
        self.number = number
    
    def fibonacci_num(self):
        fib_seq = [0,1]
        while len(fib_seq) < self.number:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    def fib3(self):
        a,b = 0,1
        fib3 = []
        for i in range(self.number):
            fib3.append(a)
            a,b = b, a+b
        return fib3

fib1 = Fib(10)
print(fib1.fibonacci_num())
fib2 = Fib(20)
print(fib2.fib3())



