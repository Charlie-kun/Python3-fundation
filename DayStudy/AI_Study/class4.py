#AI Class4 study
def get_sum(start, end):
    sum=0
    for i in range(start, end+1):
        sum+=i
    return sum

value=get_sum(1,10)
print(value)

def square(n):
    return(n*n)

print(square(10))

def get_min(x,y):
    if(x<y):
        return x
    else:
        return y

print(get_min(10,20))

def happyBirthday():
    print("HB")
    print("HB")
    print("dear my friend")
    return

happyBirthday()

def FtoC():
    x=float(input("input Fahrenheit : "))
    f=5/9*(x-32)
    return f

print(FtoC())

def is_prime():
    x=int(input("input number : "))
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

print(is_prime())

import math

def sphereVolume():
    r=int(input("imput radius : "))
    v=(4/3)*math.pi*r**3
    return v

print(sphereVolume())

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print(mul(30,add(10,20)))

def sub(x,y):
    global s

    x,y=y,x
    z="사과"
    s="바나나"
    print(z,s,x,y)

z,s,x,y=1,2,3,4
sub(7,8)
print(z,s,x,y)

def pimath():
    r=int(input("input radius : "))
    print("원의 면적 : ", r**2*math.pi)
    print("원의 둘레 : ", 2*r*math.pi)

pimath()
