'''
Saw stock table and Calculate Max profit.
input : stock price change value(list : prices)
output : stock sell profit value
'''

def max_profit(prices):
    n = len(prices)
    max_profit=0    #Max profits always 0 upper value.
    for i in range(0,n-1):
        for j in range(i+1, n):    #Stock buy i th day and sell j th day, got profits.
            profit=prices[j]-prices[i]
            if profit>max_profit:    #If profit bigger than max_profit. Change eachother
                max_profit=profit

    return max_profit


stock=[10300, 9600, 9800, 8200, 7800, 8300, 9500, 9500, 9800, 10200, 9500]
print(max_profit(stock))