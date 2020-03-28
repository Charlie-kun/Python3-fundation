#Moudle applications and package
'''
#import
import mymath
print(mymath.area(5))    #78.5

#from
from mymath import area, mypi
print(area(5))    #78.5
print(mypi)    #3.14

from mymath import *    #import all
mypi=3.25555
print(mypi)    #3.25555
'''
'''
#as
import string as chastr     #Import name change
print(chastr)    #string module display
print(chastr.punctuation)
'''
'''
#from import as
from mymath import mypi as mpi
print(mpi)

def str_test(s):    
  import string    #Able to use this.
  t=string.split(s)
  return t

import mymath    #Insert "print" in mymath
'''
'''
#If module name and use name same.
string='My first string'
import string
print(string)    #display string module
'''
'''
import string
string='My first string'
print(string)    #My first string
'''
'''
#Reused module
import string
string.a=1
string='My first string'
print(string)    #My first string

import string
print(string.a)    #1
print(string)    #stirng moudle display
'''

#Module execute and test Code
'''
import prname    #prname
print(prname.__name__)    #prname
print(__name__)    #__main__

import string
print(string.__name__)    #string

import re
print(re.__name__)    #re

import os
print(os.__name__)    #os
'''
