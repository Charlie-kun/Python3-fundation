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
