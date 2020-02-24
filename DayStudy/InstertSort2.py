'''
INSTERt sorted
input : list "a"
output : nothing
'''

def ins_sort(a):
  n=len(a)
  for i in range(1,n):    #1 to n-1
      key = a[i]    #i th position value  list key saved
      j=i-1    #j saved next to i

      while j>=0 and a[j]>key:    #find keys instert position
          a[j+1]=a[j]    # move to right one positon
          j-=1
      a[j+1]=key    #instert key

d=[2,4,5,1,3]
ins_sort(d)
print(d)    #sort [1,2,3,4,5]
