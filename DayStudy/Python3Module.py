'''
Python module

Naming space or Scope
'''
'''
#Local and Global variable.

g=10    #g, h is Global variable.
h=5

def f(a):
  h=a+10    #Local variable.
  b=h+a+g
  return b

print(f(h))     #30
print(h)    #5

def f(a):    #"a" is local variable.
  global h    #"h" is global variable.
  h=a+10
  return h

print(f(10))    #20
print(h)    #Already reported as 20.

def f():
  global g    #"g" is global variable.
  a=g    #l-values "g" is global variable.
  g=20    #r-values "g" is local variable.
  return a

print(f())
'''
'''
#Get a name list
l=[]
print(dir(l))    
'''
'''
#Functions nested scopes
x=2
def F():
  x=1
  def G():
    print(x)
  G()

F()
'''
#Module Definitions
'''
#Make a user module and call
#File: mymath.py
mypi=3.14

def add(a,b):
  return a+b

def area(r):
  return mypi*r*r

#File : test.py
import mymath

print(dir(mymath))
print(mymath.mypi)     #Variable mypi use, in mymath 
print(mymath.area(5))    #fuction area use, in mymath

import string    #python standard module
print(dir(string))
'''
'''
class C:
  a=2
  pass

c=C()
c.a=1

print(c.a)
print(c.__class__.a)    #"c" instance class
print(C.a)

x=10
def f():
  a=1
  b=2
f.c=1
print(f.c)
print(f.a)    #Can't use
'''

#Module search path
import sys
print(sys.path)

#Module search path dynamic change.
sys.path.append('~/mypythonlib')
print(sys.path)
