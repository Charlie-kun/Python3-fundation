'''
Find fake coin algorithm.
input : Total coins position, start and end.
output : Out fake coins position number
'''

'''
Weight measurement
a and b compare weight. And find a fake coin, display "-1"
c and d compare weight. And find a fake coin, display "1"
There are has not fake coin. display "0"
'''

def weigh(a,b,c,d):
  fake = 29    #fake coins position(Algorithm find this position)
  if a <= fake and fake <= b:
    return -1
  if c <= fake and fake <=d:
    return 1
  return 0

'''
Using weight method
Left to right all coins weight measurement.
'''
def find_fakecoin(left, right):
  for i in range(left+1, right+1): #Roop for weight measurement
      result = weigh(left, left, i, i)
      if result==-1:    #Left coin is light(left coin is fake)
        return left
      elif result==1:   #i coin is light (i coin is fake)
        return i    # if two coins weight is same . Compare next coin.
  
  return -1   #every coin weight has same. No fake coin

n=100    #Coins number.
print(find_fakecoin(0, n-1))
