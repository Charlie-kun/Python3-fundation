#Class and Object
'''
#Python Class and namespace
class S1:
  a=1

print(S1.a)

S1.b=2    #Create new name.
print (S1.b)

print(dir(S1))    #Search Class name
del S1.b    #Delete b in S1.
print(dir(S1))

x=S1()    #"x" is S1 class instance.
print(x.a)    #1

x.a=10    #Class instance "x" namespace to insert 10. 
print(x.a)    #10

print(S1.a)    #1, Class namespace and class instance different .

y=S1()
y.a=300
print(y.a)
print(x.a)    #x instance spacename check
print(S1.a)    #class namespace a check
'''
'''
class Simple:
  pass

s1=Simple()
s2=Simple()

s1.stack=[]
s1.stack.append(1)
s1.stack.append(2)
s1.stack.append(3)

print(s1.stack)    #[1,2,3], check s1 stack
print(s1.stack.pop())    #3, stack value pop(last append, first output)
print(s1.stack.pop())    #2

print(s1.stack)    #[1], final stack value
#print(s2.stack)    #s2 was not defined stack

del s1.stack    #s1 stack delete
'''

#General method define and calling
'''
class MyClass:
  def set(self, v):    #instance calling.
    self.value=v
  def get(self):    #instance calling.
    return self.value

c=MyClass()    #create instance
c.set('egg')    #method "set" calling
print(c.get())    #egg, method "get" calling
print(c.value)    #egg, instance parameter direct access.

c=MyClass()
MyClass.set(c, 'egg')    #It's same thing.
print(MyClass.get(c))    #egg, unbound method
print(c.value)    #egg

class Simple:
  pass

c=MyClass()
s1=Simple()
MyClass.set(s1, 'egg')   #Input different class instance will get error.
'''
'''
#Class inside calling
def set(i):    #insert after.
  print("set function outside function-", i)

class MyClass:
  def set(self, v):
    self.value=v
  def incr(self):
    #self.set(self.value+1)
    set(self.value+1)
  def get(self):
    return self.value

c=MyClass()
c.set(1)    #MyClass, set insert 1.
print(c.get())    #1

c.incr()
print(c.get())    #2, (after) 1
'''
'''
#Static method
class D:
  @staticmethod    #Decorator use.
  def spam(x,y):
     print('static method', x,y)

D.spam(1,2)    #No instance object, direct calling class.

d=D()
d.spam(1,2)    #instance object path calling possible.
'''
'''
#Class method
class C:
  @classmethod    #Decorator
  def spam(cls, y):
    print(cls, '->', y)

print(C)

C.spam(5)    #First argument passed to "C" potentially

c=C()
c.spam(5)    #Instance object pass possible to calling.

class D(C):    #Class D <- C
  pass

print(D.spam(3))

d=D()
print(d.spam(3))
'''
'''
#Class member and Instance member
class Var:
  c_mem=100    #class member define.
  def f(self):
    self.i_mem=200    #define instance member
  def g(self):
    print(self.i_mem)
    print(self.c_mem)

print(Var.c_mem)    #100

v1=Var()    #Create instance v1.
print(v1.c_mem)    #100, Class member access.
v1.f()
print(v1.i_mem)    #200, instance member access.

v2=Var()    #create instance v2
#print(v2.i_mem)    #Don't have i_mem in v2. got a error.

print(v1.c_mem)    #100,Class member reference, through to instance v1
print(v2.c_mem)    #100

v1.c_mem=50
print(v1.c_mem)    #50, instance member v1 reference, through to class member.
print(v2.c_mem)    #100
print(Var.c_mem)    #100
'''

#Constructors and destructors
from time import ctime, sleep

class Life:
  def __init__(self):    #Constructors
    self.birth=ctime()    #Get a current time
    print('Birthday', self.birth)    #display current time
  def __del__(self):    #Destructors
    print('Deathday',ctime())

def test():
  mylife=Life()
  print('Sleeping for 3 sec')
  sleep(3)    #Sleep state at 3 second(Can't access CPU).

test()

class Integer:
  def __init__(self,i):
    self.i=i
  def __str__(self):
    return str(self.i)

i=Integer(10)
print(i)    #10
print(str(i))    #10
