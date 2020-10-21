class Counter:
    def reset(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get(self):
        return self.count

a=Counter()

a.reset()
a.increment()
print("Counter a value is ", a.get())

a=Counter()
b=Counter()

a.reset()
b.reset()

class Television:
    def __init__(self, channel, volume, on):
        self.channel=channel
        self.volume=volume
        self.on=on
    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel):
        self.channel=channel
    def getChannel(self):
        return self.channel

t=Television(9,10,True)

t.show()
t.setChannel(11)
t.show()
'''
class Student:
    def __init__(self, name=None, age=0):
        self.__name=name
        self.__age=age

obj=Student()
print(obj.__age)
'''

import math
class Circle:
    def __init__(self, radius=1.0):
        self.__radius=radius

    def setRadius(self, r):
        self.__radius=r

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        area=math.pi*self.__radius**2
        return area
    def calcCircum(self):
        circumference=2.0*math.pi*self.__radius
        return circumference
    def __eq__(self, other):
        return self.__radius==other.__radius

c1=Circle(10)
print("Radius = ", c1.getRadius())
print("Circle Area = ", c1.calcArea())
print("Circumference of a circle = ", c1.calcCircum())

c1=Circle(10)
c2=Circle(10)
if c1==c2:
    print("Circle radius same.")

class BankAccount:
    def __init__(self):
        self.__balance=0

    def withdraw(self, amount):
        self.__balance -=amount
        print(amount, "dollars deposited it the bankbook.")
        return self.__balance

    def deposit(self, amount):
        self.__balance +=amount
        print(amount, "dollars are debited into the bankbook.")
        return self.__balance

a=BankAccount()
a.deposit(100)
a.withdraw(10)

class Box:
    def __init__(self, width =0, length=0, height=0):
        self.__width=width
        self.__length=length
        self.__height=height

    def setWidth(self, width):
        self.__width=width;

    def setLength(self,length):
        self.__length=length;
    def setHeight(self, height):
        self.__height=height;
    def getVolume(self):
        return self.__width*self.__length*self.__height
    def __str__(self):
        return '(%d, %d, %d)' %(self.__width, self.__length, self.__height)

box=Box(100, 100, 100)
print(box)
print("box value is", box.getVolume())

class Car:
    def __init__(self, speed=0, gear=1, color="white"):
        self.__speed=speed
        self.__gear=gear
        self.__color=color

    def setSpeed(self, speed):
        self.__speed=speed

    def setGear(self,gear):
        self.__gear=gear

    def setColor(self,color):
        self.__color=color

    def __str__(self):
        return '(%d, %d, %s)' %(self.__speed, self.__gear, self.__color)

myCar=Car()
myCar.setGear(3)
myCar.setSpeed(100)
print(myCar)

# Special Method
class Vector2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y -other.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __str__(self):
        return '(%g, %g)' %(self.x, self.y)

u=Vector2D(3,1)
v=Vector2D(1,0)
w=Vector2D(1,1)
a=u-v
print( a)
