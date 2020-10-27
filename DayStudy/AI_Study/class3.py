# Control
x=int(input("Integer x= "))

if(x%2==1):
    print("Odd Number")
else:
    print("Even Number")

score=int(input("Input Score : "))

if(score>=90):
    print("A Grades")
elif(score>=80):
    print("B Grades")
elif(score>=70):
    print("C Grades")
elif(score>=60):
    print("D Grades")
else: print("F Grades")

# Loop
sum=0
i=1
while(i<=100):
    sum+=i
    i+=1
print("1+2+...+100=", sum)

sum=0
for i in range(1,101):   #Important is last 101.
    sum+=i
print("1+2+...+100 = ", sum)
print("1+2+...+100 =" +str(sum))
'''
import turtle
t=turtle.Pen()

while True:
    direction = input("Left=left, Right=right : ")
    if direction=="left":
        t.left(60)
        t.forward(50)
    if direction=="right":
        t.right(60)
        t.forward(50)
'''
x=int(input("First integer : "))
y=int(input("Second integer : "))

if (x>y):
    max=x;
else :
    max=y;
print("Big integer is ",max);

str=input("Input string : ")
length=len(str)
if length%2==1:
    ch1=str[length//2]
    print("Center char is ", ch1)
else:
    ch1=str[length//2-1]
    ch2=str[length//2]
    print("Center char is", ch1, ch2)

credits=float(input('input your score : '))
gpa=float(input("Input your grade point average : "))
if credits>=140 and gpa>=2.0:
    print("Possible to graduate!")
else :
    print("Impossible to graduate!")

appleQuality=input("Input apple's quality : ")
applePrice=int(input("Input an apple price : "))
if appleQuality =="Good":
    if applePrice<1000:
        print("Buy 10 apples.")
    else:
        print("Buy 5 apples.")
else:
    print("Don't buy appeles.")

for x in[0,1,2,3,4,5,6,7,8,9]:
    print(x, end=" ")


sum=0
for x in range(10):
    sum=sum+x
print(sum)

import math
import turtle

t= turtle.Turtle()

t.pendown()
for angle in range(360):
    y=math.sin(math.radians(angle))
    scaledX=angle
    scaledY=y*100
    t.goto(scaledX, scaledY)
t.penup()
