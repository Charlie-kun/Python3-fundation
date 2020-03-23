'''
# "List" Basic
l=[1,2, "Great"]

print(l[0], l[-1])
print(l[1:3], l[:])    #list range output, list output no option
print()

L=range(10)
print(list(L[::2]))    #Range List output
print()

print(l*2)    #List *
print(l+[3,4,5])    #List +
print(len(l))
print()
print(4 in L)    #True
'''

'''
#"List" have a Mutable property.
a=['spam', 'eggs', 100, 1234]
a[2]=a[2]+23
print("a is ",a)

b=[1,12,123,1234]
b[0:2]=[]
print("b is ", b)
'''

'''
#Slice input
a=[123,1234]    
a[1:1]=['spam', 'ham']    #1 to 1, so insert 'spam, ham' at 1 position.
print("a is ",a)

b=[123,1234]
b[1:2]=['spam', 'ham']   #1 to 2, so modify 'spam, ham' at 1234.
print("b is ", b)

a[0:0]=a    #forward for "a" add "a".
print(a)
'''

'''
#Delete
a=[1,2,3,4]
del a[0]
print("del a[0] : ", a)

del a[1:]
print("del a[1:] : ", a)

b=range(4)
print("b : " ,list(b))
print("b[::2] : ", b[::2])

#del b[::2]
#print("del b[::2] : ",list(b))    #Python3 don't support range del. 

del b    #Delete  list "b"
'''

'''
#Nested list
s=[1,2,3]
t=['begin', s, 'end']
print(t)
print(t[1][1])    #Choose parameter position 1at list "s" in list.

s[1]=100
print(t)
'''


#Tuple
lt=[('one', 1), ('two', 2), ('three', 3)]
for t in lt:
  #print('name=', t[0], ', num=',t[1])
  print('name = %s, num=%s' % t)
