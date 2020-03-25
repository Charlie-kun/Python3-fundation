#Define function and calling
'''
def add(a,b):
  return a+b

print(add(1,2))

def myabs(x):
  if x<0:
    x=-x
  return x

print(abs(-4))
print(myabs(-4))
'''
'''
#Define Empty function
def simpleFuction():
  pass

simpleFuction()
'''
'''
#Define list function
def addmember(members,newmember):
  if newmember not in members:
    members.append(newmember)

members=['hwang', 'lee', 'park', 'youn']   #initial list

addmember(members,'jo')    #insert new mebmer

addmember(members, 'hwang')

print(members)
'''
'''
#Call by Reference
def fl(b):    #integer
  b=100

a=200
fl(a)
print(a)    #a=200

def f2(b):    #string
  b="abc"

a="def"
f2(a)
print(a)    #def

def f3(b):    #tuple
  b=(1,2,3)

a=(4,5,6)    #Can't chage tuple
f3(a)
print(a)    #(4,5,6)

def f4(b):    #list
  b[1]=10    #Can change list element!

a=[4,5,6]
f4(a)
print(a)    #[4,10,6]

def f5(b):    #Dictionary
  b['a']=10    #Can change Dictionary value!

a={"a":1, "b":2}
f5(a)
print(a)    #{'a':10, 'b':2}
'''
'''
#Return
def nothing():
  return

print(nothing())    #None

def print_menu():
  print("1. Stack")
  print("2. Snack")
  print("3. Snick")
  #return    #Same thing

a=print_menu()
print(a)    #return None

def myabs(x):
  if x<0 : return -x
  return x

print(myabs(-13))    #13

def swap(x,y):
  return y,x    #return tuple type

a=10
b=20
print(a,b)    #10 20

a,b=swap(a,b)
print(a,b)    #20 10

x=swap(a,b)
print(x[0], x[1])    #Again swapped. 10 20 

#New list return
def length_list(l):
  res=[]
  for el in l:
    res.append(len(el))
  return res

l=['python', 'pyson', 'pythong', 'pydon']
print(length_list(l))
print([len(s) for s in l])    #in the list
'''

#Dynamic type decision of function argument.
def add(a,b):
  return a+b

c=add(1,3.4)
d=add('dynamic', 'typing')
e=add(['list'], ['and', 'list'])
print(c)
print(d)
print(e)
