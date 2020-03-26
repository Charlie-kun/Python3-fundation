#Lambda function
'''
f=lambda x:x+1
print(f(4))    #5

g=lambda x,y: x+y
print(g(1,2))    #3

#Basic argument
incr=lambda x, inc=1:x+inc
print(incr(10))    #11
print(incr(10,5))    #15

#Dynamic argument
vargs=lambda x, *args:args
print(vargs(1,2,3,4,5))    #(2,3,4,5)
'''

#Using lambda function
'''
#Not using lambda function
def f1(x):
  return x*x +3*x -10

def f2(x):
  return x*x*x

def g(func):
  return [func(x) for x in range(-10, 10)]

print(g(f1))
print(g(f2))
'''
'''
#Using lambda function
def g(func):
  return [func(x) for x in range(-10, 10)]

print(g(lambda x:x*x+3*x-10))
print(g(lambda x:x*x*x))
'''
'''
#Using lambda list
func=[lambda x, y: x+y, lambda x,y:x-y, lambda x,y:x*y, lambda x,y:x/y]    #list

def menu():
  print("0. add")
  print("1. sub")
  print("2. mul")
  print("3. div")
  print("4. quit")
  return int(input('Select menu : '))

while 1:    #Unlimit roop
  sel = menu()
  if sel > len(func) or sel < 0 :
    continue
  if sel == len(func):
    break
  x=int(input('First operand : '))
  y=int(input('Second operand : '))
  print('Result = ', func[sel](x,y))
'''

#Using lambda function
'''
#map function
def f(x):
  return x*x

X=[1,2,3,4,5]    #list
Y=list(map(f,X))
print(Y)    #[1,4,9,16,25]

#Not using map function
def f(x):
  return x*x

X=[1,2,3,4,5]
Y=[]
for x in X:
  y=f(x)
  Y.append(y)
print(Y)
'''
'''
#map+lambda function
X=[1,2,3,4,5]
print(list(map(lambda x:x*x,X)))

Y=list(map(lambda x:x*x+4*x+5,range(10)))
print(Y)    #[5,10,17,26,37,50,65,82,101,122]

y=list(map(lambda x: len(x), ['Hello', 'Python', 'Programming']))
print(y)
'''
'''
#Fileter fuction
print(list(filter(lambda x: x>2, [1,2,3,34])))

#Not using filter function
y=[]
for x in [1,2,3,34]:
  if x>2:
    y.append(x)
print(y)
'''
'''
#Odd numbers selector.
print(list(filter(lambda x:x%2, [1,2,3,4,5,6])))

#Even numbers selector.
print(list(filter(lambda x:x%2-1,[1,2,3,4,5,6])))

#Range numbers filtering.
def F():
  x=1
  print(list(filter(lambda a:a>x, range(-5,5))))

F()

print(list(filter(lambda x: x>2, [1,2,3,34])))    #list
print(tuple(filter(lambda x:x>2, (1,2,3,34))))    #tuple
print(list(filter(lambda x:x<'a', 'abcABCdefDEF')))   #string=char list
'''

#Reduce function
from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))   #Return one value. 15

print(reduce(lambda x,y:x+y,[1,2,3,4,5],100))   #115. 100 is first value.

print(reduce(lambda x,y : x+y*y, range(1,11),0))    #385

x=0
for y in range(1,11):
  x=x+y*y
print(x)    #385

#Reverse str
print(reduce(lambda x,y:y+x,'abcde'))    #edcba

