'''
Find number
list "a", Find number index "x".
If you find number "x" display  "x" position, but  display "-1" is can't find number case.
'''

def serch_list(a,x):
  n=len(a)    #input size 'n'
  for i in range(0,n):     #list "a" sort
    if x==a[i]:    #Compare with "x" and "list a".
        return i    #Same return



  return -1     #Anything can't find Number return -1

v=[17,92,18,33,58,7,33,42]

print(serch_list(v,18))    #2
print(serch_list(v,900))    #-1
