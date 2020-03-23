#Use tuple
t1=[1, 2, 3, 4, 5]
t2=[3, 4, 5, 6, 7]
s1 = set(t1)
s2 = set(t2)
s3 = s1.symmetric_difference(s2)    #Excepted overlap numbers.
t3 = list(s3)
print(t3)

#t3=t1+t2
#print(t3)

#Use dictionary
d = {'aaa':1, 'eee':5, 'bbb':2, 'ddd':4, 'ccc':3}

for y,v in sorted(d.items(), key=lambda d:d[1]):
  print(y,v)
