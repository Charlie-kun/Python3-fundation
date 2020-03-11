'''
Max profit calculate speed compare.
Max profit exam solve speed  compare O(n*n), O(n).
'''

import time    #Time measure method.
import random    #Need to "test stock list" made.

def max_profit_slow(prices):    #O(n*n) algorithm
  n=len(prices)
  max_profit=0

  for i in range(0, n-1):
    for j in range(i+1, n):
      profit=prices[j]-prices[i]
      if profit>max_profit:
        max_profit=profit
  return max_profit

def max_profit_fast(prices):
  n=len(prices)
  max_profit=0
  min_price=prices[0]

  for i in range(1,n):
    profit=prices[i]-min_price
    if profit>max_profit:
      max_profit=profit
    if prices[i]<min_price:
      min_price=prices[i]

  return max_profit


def test(n):    #Make a test list.
  a=[]
  for i in range(0,n):
    a.append(random.randint(5000, 20000))
    start=time.time()    #Memorize calcullation start time.
    mps=max_profit_slow(a)    #Calculation slow start.
    end=time.time()    #Memorize calculation end time.
    time_slow=end-start    #Total calculate time.
    start=time.time()    #Memorize calcullation start time.
    mpf=max_profit_fast(a)    #Calculation fast start.
    end=time.time()    #Memorize calculation end time.
    time_fast=end-start    #Total calculate time.  
    print(n,mps,mpf)    #Input size and each calculate value same.
    m=0    #Compare to slow algorithm and fast algorithm.
    if time_fast>0:
      m=time_slow/time_fast
    print("%d, %.5f %5f %.2f" %(n, time_slow, time_fast, m))

test(100)
