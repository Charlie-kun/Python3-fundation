#Class and Duplicate operator definition
'''
class Integer:
  def __init__(self,i):
    self.i=i
  def __str__(self):
    return str(self.i)
  def __add(self, other):
    return self.i+other

i=Integer(10)
print(i)    #10
print(str(i))    #10


i=int(str(i))+10    #python3 need str(i) and type change
print(i)    #20

i+=10
print(i)    #30
'''
'''
class MyString:
  def __init__(self,str):
    self.str=str
  def __truediv__(self,sep):    #python3 use __turediv__ it means "/"
    return self.str.split(sep)
  __rtruediv__=__truediv__    #Right side same left side
  def __neg__(self):
    t=list(self.str)
    t.reverse()
    return ''.join(t)
  __invert__=__neg__    #'~'is same '-'
  

m=MyString("abcd_abcd_abcd")
print(m/"_")    #['abcd','abcd','abcd']
print(m/"_a")    #['abcd','bcd','bcd']
print(m.__truediv__("_"))    #['abcd','abcd','abcd']

print("_"/m)    #['abcd','abcd','abcd']
print("_a"/m)    #['abcd','bcd','bcd']

print(-m)    #dcba_dcba_dcba
print(~m)    #dcba_dcba_dcba
'''
'''
#Duplicate Compare operator.
class MyCmp:    #python3 no longer use __cmp__
  def __eq__(self, y):   #equal
    return 1===y
  def __lt__(self, y):    #self<other
    return 1<y
  def __le__(self, y):    #self<=other
    return 1<=y
  def __ne__(self, y):    #self!=other
    return 1!=y  
  def __gt__(self, y):    #self>other
    return 1>y
  def __ge__(self, y):    #slef>=other
    return 1>=y

c=MyCmp()
print(c>10)    #False, c.__cmp__(10)calling
print(c<10)    #True, c.__cmp__(10)calling
print(c==10)    #False, c.__cmp__(10)calling
'''
'''
#Operator duplicate of "Sequence/Mapping data type"
class Square:
  def __init__(self, end):
    self.end=end
  def __len__(self):
    return self.end
  def __getitem__(self, k):    
    if k<0 or self.end<=k:    #make error
      raise IndexError(k)
    return k*k

s1=Square(10)
print(len(s1))    #10, s1.__len__()
print(s1[1])    #1, s1.__getitem__(1)
print(s1[4])    #16
#print(s1[20])    #error message

for x in s1:
  print(x)    #0 1 4 9 16 25 36 49 64 81

print(list(s1))    #[0 1 4 9 16 25 36 49 64 81]
print(tuple(s1))    #(0 1 4 9 16 25 36 49 64 81)
'''
'''
#Mapping data type operator Duplicate
class MyDict:
  def __init__(self, d=None):
    if d==None:d={}
    self.d=d
  def __getitem__(self, k):    #key
    return self.d[k]
  def __setitem__(self, k, v):
    self.d[k]=v
  def __len__(self):
    return len(self.d)
  def keys(self):
    return self.d.keys()
  def values(self):
    return self.d.values()
  def items(self):
    return self.d.items()

m=MyDict()    #__init__
m['day']='light'    #__setitem__
m['night']='darkness'    #__setitem__
print(m)
print(m['day'])    #light, __getitem__
print(m['night'])    #darkness, __getitem__
print(len(m))    #2, dictionary length

z=MyDict({'one':1, 'two':2, 'three':3})
print(list(z.keys()))    #python3 need to list in dictionary display
print(list(z.values()))
print(list(z.items()))
'''
'''
#Transform for string, calling  object
class StringRepr:
  def __repr__(self):
    return 'repr called'
  def __str__(self):    #general use
    return 'str called'

s= StringRepr()
print(s)    #str called
print(str(s))    #str called
print(repr(s))    #repr called
'''
'''
class StringRepr:
  def __repr__(self):
    return 'repr called'

s=StringRepr()
print(s)    #repr called
print(str(s))    #repr called
print(repr(s))    #repr called
'''
'''
class StringRepr:
  def __str__(self):    #general use
    return 'str called'

s=StringRepr()
print(s)    #str called
print(str(s))    #str called
print(repr(s))    #object type called
'''
'''
#Make a calling class instance.
class Accumulator:
  def __init__(self):
    self.sum=0
  def __call__(self, *args):
    self.sum += sum(args)
    return self.sum

acc=Accumulator()
print(acc(1,2,3,4,5))
print(acc(6))
print(acc(7,8,9))
print(acc.sum)
'''

#Check for calling class
def check(func):
  if callable(func):
    print('callable')
  else:
    print('not callable')

class B:
  def func(self,v):
    return v
class A:
  def __call__(self, v):
    return v

a=A()    #callable
b=B()    #not callable
check(a)
check(b)

print(callable(a))    #True
print(callable(b))    #False
