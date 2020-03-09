'''
Show the stock table and make max profit algorithm.
input : Stock table(list : prices)
output : Trade stock and get a max profit.
'''

def max_profit(prices):
  n=len(prices)
  max_profit=0    #Max profit is always over the 0.
  min_price=prices[0]    #Get a first day stock value.
  for i in range(1,n):    #Repeat 1 to n-1.
    profit=prices[i]-min_price   #Compare prices
    if profit > max_profit:    #If profit bigger than max_profit replaced.
      max_profit = profit
    if prices[i] < min_price:    #If profits smaller than min_price replaced.
      min_price = prices[i]

  return max_profit

stock=[10300,9600,9800,8200,7800,8300,9500,9800,10200,9500]
print(max_profit(stock))
