# Fctorial

def fac(n):
    f=1    #multiplication first number
    for i in range(1, n+1):
        f=f*i    #modified multiplication
    return f

print(fac(1))
print(fac(10))    # result is 3628800


def fact(n):
    if n<=1:     # end condition
        return 1
    return n*fact(n-1)    #Recursive Function

print(fact(5))    # result is 120


