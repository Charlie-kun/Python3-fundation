# 1 to n continue number sum
'''
def sum_n(n):
  s=0     #save to sum result
  for i in range(1,n+1):    #repeat to 1 to n(Not n+1)
      s=s+i
  return(s)

print(sum_n(10))    # 1 to 10 sum
print(sum_n(100))    # 1 to 100 sum

def sum_n1(n):
  return n*(n+1)//2    # two slash mean's Division of integers

print(sum_n1(10))    # 1 to 10 sum
print(sum_n1(100))    # 1 to 100 sum

#sum_n1 better than sum_n because Calculate simple!
'''

'''
# using list
a=[5,7,9]
print(a)
print(a[0])    # 0th list "a" element. '5'
print(a[2])    # 2nd list "a" element. '9'
print(a[-1])    # last list "a" element. '9'
print(len(a))    # length for list "a"

a.append(4)    #append element '4' in "a"
print(a)
a.insert(0,10)    # 0th location insert '10' in "a"
print(a)

print(a.pop())    # no chose pop() number. so last element print
print(a.pop(3))    # chose pop() number '3' so print 3th list "a" element. '9'

print(2 in a)    # check at list "a" for "2". Answer is ture or flase. 'false'

a.clear()    # Delect all element in "a". 
print(a)    #'[]'
'''

'''
# Find Maximum Value

v=[17,92,18,33,58,7,33,42]    # find maximum value in list "v"

def find_max(a):
  n=len(a)    # input list length
  max_v=a[0]    # list's 0th element chose and memorize max_v
  for i in range(1,n):    # repate a to n
    if a[i]>max_v:    # if element a[i] find bigger then max_v
      max_v=a[i]    # change max_v to a[i]
  return max_v

print(find_max(v))    #'92'
'''

#Find Maximum Vlaue's position

v=[17,92,18,33,58,7,33,42]    # find maximum value in list "v"
def find_max(a):
  n=len(a)    # input list length
  count=0
  max_v=a[0]    # list's 0th element chose and memorize max_v
  for i in range(1,n):    # repate a to n
    if a[i]>max_v:    # if element a[i] find bigger then max_v
      max_v=a[i]    # change max_v to a[i]
      count=i
  return count

print(find_max(v))    #'1'
