'''
MergeSort
input : list "a"
output : nothing
'''

def merge_sort(a):
  n=len(a)
  if n<=1:    # Finish Condition
    return
  mid=n//2    #Divide one group by two group 
  g1=a[:mid]
  g2=a[mid:]
  merge_sort(g1)    #Recursive call for first group
  merge_sort(g2)    #Recursive call for second group
  i1=0 
  i2=0 
  ia=0
  while i1<len(g1) and i2<len(g2):
    if g1[i1]<g2[i2]:
      a[ia]=g1[i1]
      i1 +=1
      ia+=1
    else:
      a[ia]=g2[i2]
      i2+=1
      ia+=1
  while i1<len(g1):   #Remaining Data insert to "result"
    a[ia] = g1[i1]
    i1+=1
    ia+=1
  while i2<len(g2):
    a[ia]=g2[i2]
    i2+=1
    ia+=1

d=[6,8,3,9,10,1,2,4,7,5]
merge_sort(d)
print(d)    #[1,2,3,4,5,6,7,8,9,10]
