'''
Easy explain for quick sort
input: list "a"
output : sorted new list
'''

def quick_sort(a):
  n=len(a)
  if n <=1:    #Condition for quit
    return a     

  pivot=a[-1]    #Easy choose to last component.
  g1=[]    #group 1 : chose standard component smaller than others.
  g2=[]    #group 2 : chose standard component bigger than others.
  for i in range(0, n-1):    #last component is standard.
    if a[i]<pivot:    #Compare for standard component.
      g1.append(a[i])    #Smaller than pivot is add to g1.
    else:
      g2.append(a[i])    #Bigger than pivot is add to g2.
  return quick_sort(g1)+[pivot]+quick_sort(g2)


d=[6,8,3,9,10,1,2,4,7,5]
print(quick_sort(d))
