#Weak Reference,Iterator,Generator
'''
#Weak reference Module
import sys
import weakref
class C:
  pass

c=C()    #create class
c.a=1    #test value insert at instance c 
print("refcount -", sys.getrefcount(c))    #2, Checking object c reference count.

d=c    #General reference count increase
print("refconut -", sys.getrefcount(c))   #3

r=weakref.ref(c)    #Create Weak reference object "r". 
print("refconut -", sys.getrefcount(c))    #3, Count not changed.

print(r)    #weak reference object
print(r())    

print(c)
print(r().a)    #1

del c    #delete object
del d
print(r())    #None return
#print(r().a)    #Can't display property, error

d={'one':1, 'two':2}    #None
wd=weakref.ref(d)    #error
'''
'''
import sys
import weakref
class C:
  pass

c=C()
c.a=2
print("refcount -", sys.getrefcount(c))    #2, Search reference count at object "c".
p=weakref.proxy(c)    #Create proxy object
print("refcount -", sys.getrefcount(c))    #2, Don't change count

print(p)
print(c)
print(p.a)    #2
'''
'''
import weakref
class C:
  pass

c=C()
r=weakref.ref(c)   #Create weakref
p=weakref.proxy(c)   #create weakref proxy
print(weakref.getweakrefcount(c))    #2, weakref count
print(weakref.getweakrefs)    #Search weakref list.
'''
'''
#Weak Dictionary
import weakref
class C:
  pass

c=C()
c.a=4
d=weakref.WeakValueDictionary()    #create WeakValueDictionary
#d={}    #create general dict 
print(d)

d[1]=c
print(d.items())    #display dict
print(d[1].a)    #4

del c
print(d.items())    #both of not empty
'''
'''
#Iterator
I=iter([1,2,3])
print(I)

print(I.__next__())    #python3 need
print(I.__next__())
print(I.__next__())
#print(I.__next__())    #Not exist, error
'''
'''
def f(x):
  print(x+1)

for x in [1,2,3]:
  f(x)
'''
'''
def f(x):
  print(x+1)    #2,3,4

t=iter([1,2,3])
while 1:
  try:
    x=t.__next__()
  except StopIteration:
    break
  f(x)    
'''
'''
def f(x):
  print(x+1)

for x iter [1,2,3]:
  f(x)
'''
'''
# Iterator Class
class Seq:
  def __init__(self, fname):
    self.file =open(fname)
    #def __getitem__(self, n):
    #   if n==10:    #raise StopIteration
    #   return n
  def __iter__(self):
    return self
  def __next__(self):
    line=self.file.readline()
    if not line:
      raise StopIteration
    return line

s=Seq('readme.txt')
for line in s:
  print(line)

print(Seq('readme.txt'))
print(list(Seq('readme.txt')))
print(tuple(Seq('readme.txt')))
'''
'''
#Dictionary iterator
d={'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
for key in d:
  print(key,d[key])
'''
'''
d={'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
for key in iter(d):
  print(key,d[key])

for key in d.keys():    #in Python3 iterkeys->keys
  print(key)

keyset=d.keys()
print(next(iter(keyset)))    #one, in Python3.
for key in keyset:
  print(key)

for value in d.values():   #in pyhton3
  print(value)

for key, value in d.items():    #in python3
  print(key, value)
'''
'''
#File Iterator
f=open('readme.txt')
print("f.__next__()", f.__next__())
for line in f:
  print(line)
'''

#Generator
'''
def f(a,b):
  c=a*b
  d=a+b
  return c,d

def general_ints(N):
  for i in range(N):
    yield i     #important to generator

gen=general_ints(3)

print(gen)
print(gen.__next__())    #0
print(gen.__next__())    #1
print(gen.__next__())    #2

for i in general_ints(5):
  print(i)    #0,1,2,3,4
'''
'''
print([k for k in range(100) if k % 5==0])

a=(k for k in range(100) if k%5==0)
print(a)
print(a.__next__())    #0
print(a.__next__())    #5
print(a.__next__())    #10
for i in a:
  print(i)    #15~95
'''
'''
print(sum((k for k in range(100) if k%5==0)))    #950

def fibonacci(a=1, b=1):
  while 1:
    yield a
    a,b=b,a+b

for k in fibonacci():
  if k>100:
    break
  print(k)
'''
'''
class Odds:
  def __init__(self, limit=None):
    self.data= -1
    self.limit=limit
  def __iter__(self):
    return self
  def __next__(self):    #in Python3
    self.data+=2
    if self.limit and self.limit <=self.data:
      raise StopIteration
    return self.data

for k in Odds(20):
  print(k)

print(list(Odds(20)))
'''

def odds(limit=None):
  k=1
  while not limit or limit >=k:
    yield k 
    k+=2

for k in odds(20):
  print(k)

print(list(odds(20))) 
