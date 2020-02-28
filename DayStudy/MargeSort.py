'''
Marge sort
input : list "a"
output : sort new list
'''

def marge_sort(a):
  n=len(a)
  if n<=1:    #End condition
    return a  
  mid=n//2
  g1=marge_sort(a[:mid])    #Recursive call. 1st group sort
  g2=marge_sort(a[mid:])    #Recursive call. 2nd group sort  
  result=[]    #g1+g2= final result.
  while g1 and g2:    #if remain component in g1 and g2 repeat.
    if g1[0]<g2[0]:    #compare g1 first component to g2 first component
      result.append(g1.pop(0))    #pick up component when g1 component smaller then g2 component
    else :
      result.append(g2.pop(0))    #pick up component when g2 component smaller then g1 component      
  while g1:
    result.append(g1.pop(0))    
  while g2:
    result.append(g2.pop(0))
  return result

d=[6,8,3,9,10,1,2,4,7,5]
print(marge_sort(d))
