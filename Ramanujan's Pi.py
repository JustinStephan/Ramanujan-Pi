import math

def babylon(n, x, y):
    if abs(x-y) <= 0.0000001:
        return x
    else:
        x = (x+y)/2
        y = n/x
        #print("x:",x," y:",y," n:",n)
        return babylon(n,x,y)

def factorial(n):
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 2
    else:
        return n * factorial(n-1)


termA = (babylon(8,5,1))/9801

print(factorial(100))