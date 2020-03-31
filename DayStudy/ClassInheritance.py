#Class Inheritance
'''
class Person:
  def __init__(self,name, phone=None):
    self.name=name
    self.phone=phone
  def __str__(self):
    return '<person %s %s>' % (self.name, self.phone)

class Employee(Person):    #inside () class means "Super class"
  def __init__(self, name, phone, position, salary):
    Person.__init__(self, name, phone)    #Person class creator calling
    self.position=position
    self.salary=salary

pl=Person('Krystal', 1994)
print(pl.name)    #Krystal
print(pl)    #<person Krystal 1994>

m1=Employee('SooJung', 1994, 'actoress', 200)
m2=Employee('Krystal', 1994, 'Singer', 300)
print(m1.name, m1.position)    #SooJong, Each displayed superclass and subclass
print(m1)    #<person SooJung 1994>
print(m2.name, m2.position)    #Krystal Singer
print(m2)    #<person Krystal 1994>
'''
'''
#Creator calling
class Super:
  def __init__(self):
    print('Super init called')

class Sub(super):
  def __init__(self):
    Super.__init__(self)    #ecept version
    print('Sub init called')

s=Sub()    #super init called, sub init called
'''
'''
#Medhod override
class Person:
  def __init__(self, name, phone=None):
    self.name=name
    self.phone=phone
  def __str__(self):
    return '<Person %s %s>' % (self.name,self.phone)

class Employee(Person):
  def __init__(self, name, phone, position, salary):
    Person.__init__(self, name, phone)
    self.position=position
    self.salary=salary

p1=Person('galee', 5284)
m1=Employee('kslee', 5224, 'President', 500)

print(p1)
print(m1)
'''
'''
class Person:
  def __init__(self, name, phone=None):
    self.name=name
    self.phone=phone
  def __str__(self):
    return '<Person %s %s>' % (self.name,self.phone)

class Employee(Person):
  def __init__(self, name, phone, position, salary):
    Person.__init__(self, name, phone)
    self.position=position
    self.salary=salary
  def __str__(self):
    return'<Employee %s %s %s %s>' % (self.name, self.phone, self.position, self.salary)

p1=Person('galee', 5284)
m1=Employee('kslee', 5224, 'President', 500)

print(p1)
print(m1)
'''
'''
#Polymorphism
class Animal:
  def cry(self):
    print('...')

class Dog(Animal):
  def cry(self):
    print('Bowow')

class Duck(Animal):
  def cry(self):
    print('cackle')

class Fish(Animal):
  pass

for each in (Dog(), Duck(), Fish()):    #Polymorphism
  each.cry()    #override
'''

#Inside class and class united
'''
a=list()
print(a)
print(dir(a))

class Mylist(list):
  def __sub__(self, other):    # '_' argument repeat method.
    for x in other:
      if x in self:
        self.remove(x)    #Each lilst element delete.
    return self

L=Mylist([1,2,3, 'spam', 4, 5])
print(L)
L=L-['spam', 4]
print(L)
'''
'''
#stack
class Stack(list):
  push=list.append

s=Stack()

s.push(4)    
s.push(5)    
print(s)    #[4,5]

s=Stack([1,2,3])
s.push(4)    
s.push(5)    
print(s)    #[1,2,3,4,5]

print(s.pop())    #5
print(s.pop())    #4
print(s)    #[1,2,3]
'''
'''
#Queue
class Queue(list):
  enqueue=list.append
  def dequeue(self):
    return self.pop(0)

q=Queue()
q.enqueue(1)    #insert data(=append)
q.enqueue(2)
print(q)    #[1,2]

print(q.dequeue())    #1    #output data
print(q.dequeue())    #2
'''
'''
a=dict()
print(a)
print(dir(a))
'''
'''
class MyDict(dict):
  def keys(self):
    K=dict.keys(self)    #unbound method calling
    sorted(K)    #pyhton3 sorted
    return K

d=MyDict({'one':1, 'two':2, 'three':3})
print(list(d.keys()))

d2={'one':1, 'two':2, 'three':3}
print(list(d2.keys()))
'''
'''
#Get a class information
print(isinstance(123,int))    #True
print(int)    #<class 'int'>

class A:
  pass
class B:
  def f(self):    #method
    pass

class C(B):    #super class B
  pass

def check(obj):
  print(obj,'=>')
  if isinstance(obj, A):    # Check class A, B, C.
    print('A')
  if isinstance(obj, B):
    print('B')
  if isinstance(obj, C):
    print('C')

a=A()
b=B()
c=C()

check(a)    #A
check(b)    #B
check(c)    #B, C
'''

class A:
  pass
class B:
  def f(self):    #method
    pass

class C(B):    #super class B
  pass

def check(obj):
  print(obj,'=>')
  if issubclass(obj, A):    # Check class A, B, C.
    print('A')
  if issubclass(obj, B):
    print('B')
  if issubclass(obj, C):
    print('C')

check(A)    #A
check(B)    #B
check(C)    #B, C
