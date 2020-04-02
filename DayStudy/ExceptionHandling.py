#Exception Handling
'''
#4+spam*3    #Name error 

#a=10    
#b=0
#c=a/b    #ZeroDivisionError

#[note] Exception ending
def division():
  for n in range(0,5):
    print(10.0/n)

division()

'2'+2    #type error, str+int

l=[1,2]
print(l[2])    #IndexError, no exist l[2]

d={"a":1, "b":2}
print(d{'c'})    #keyError, no exist c

a=open('aaa.txt')    #IOError, no exist file
'''

#Use try/except/else/finally
'''
try:
  print(1.0/0.0)
except ZeroDivisionError:
  print('zerodivison error!!')    #not finished program
'''
'''
def division():
  for n in range(0,5):
    try:
      print(10.0/n)
    except ZeroDivisionError as msg:    #in Python3
      print(msg)

division()
'''
'''
def division():
  for n in range(0,5):
    try:
      print(10.0/n)
    #else:    #SyntaxError
    finally:    #display "Success"
      print("Success")

division()
'''
'''
try:
  spam()
except NameError as msg:
  print('Error - ', msg)

def zero_division():
  x=1/0

try:
  zero_division()
except ZeroDivisionError as msg:
  print('zero division error!!! - ', msg)
  '''
'''
try:
  spam()
  print(1.0/0.0)
except:
  print('Error')
'''
'''
b=0.0
name='aaa.txt'
try:
  print(1.0/b)
  spam()
  f=open(name, 'r')
  '2'+2
except NameError:
  print('NameError!!')
except ZeroDivisionError:
  print('ZeroDivisionError')
except (TypeError, IOError):
  print('TypeError or IOError')
else:
  print('No Excception')
finally:
  print('Exit!')
  '''
'''
import os
print(os.getcwd())    #current working directory
filename='t.txt'

try:
    f=open(filename, 'r')    #This is necessary.
except IOError as msg:
    print(msg)
else:
  a=float(f.readline())
  try:
    answer=1.0/a
  except ZeroDivisionError as msg:
    print(msg)
  else:
    print(answer)
  finally:
    print("Finally!!")
    f.close()
'''
'''
#Arithmetic Exception occured
def dosomething():
  a=1/0

try:
  dosomething()
except ArithmeticError:
  print('ArithmeticException occured')
'''
'''
def dosomething():
  a=1/0

try:
  dosomething()
except ZeroDivisionError:
  print('ZeroDivisionError')
except AttributeError:
  print('ArithmeticError')
'''
'''
#Exception occured
class SquarSeq:
  def __init__(self, n):
    self.n=n
  def __getitem__(self, k):
    if k>=self.n or k<0:
      raise IndexError    #Raise Exception occured
    return k*k
  def __len__(self):
    return self.n

s=SquarSeq(10)
print(s[2], s[4])
for x in s:
  print(x)
print(s[20])    #indexerror
'''
'''
#User define Exception occured
class Big(Exception):
  pass

class Small(Big):
  pass

def dosomething1():
  x=Big()
  raise x

def dosomething2():
  raise Small()

for f in (dosomething1, dosomething2):
  try:
    f()
  except Big:
    print("Exception occured!")

'''

#Exception value send
def f():
  raise Exception("message!!!")    #in Python3

try:
  f()
except Exception as a:
  print(a)


a=10
b=0
try:
  if b==0:
    raise ArithmeticError('Dividing for 0')
  a/b
except ArithmeticError as v:
  print(v)
