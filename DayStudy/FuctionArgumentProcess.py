#Function argument Process
'''
#Basic argument value
def incr(a, step=1):
  return a+step

b=1
b=incr(b)    #increase 1
print(b)

b=incr(b,10)    #increase 10
print(b)

#def incr(step=1,a):    #Make error
  #return a+step

def area(height, width):
  return height*width

#Not important to "arguments" positions
a=area(height='height string ', width=3)
print(a)

b=area(width=20, height=10)
print(b)

#print area(20, width=5)    #make error

def incr(a,step=1, step2=10, step3=100):
  return a+step+step2+step3

print(incr(10,2,step2=100))    #212
#print(incr(10,2,step2=100,200))    #make error. keyword argument is don't position to center.
'''
'''
#Dinamic argument list
def varg(a, *arg):   #*arg means "get a tuple type value"
  print(a,arg)
  print(arg[0], arg[1])    #Use tuple tpye.

#varg(1)
#varg(2,3)
varg(2,3,4,5,6)

def printf(formet, *args):
  print(formet % args)

printf("i've spent %d days and %d night to do this", 6,5)    #Make a Similar to C language method.
'''

#Tuple argument and Dictionary argument calling
def h(a,b,c):    
  print(a,b,c)

args=(1,2,3)    #tuple
h(*args)
h(args[0],args[1],args[2])

dargs={'a':1, 'b':2, 'c':3}    #dictionary
h(**dargs)
