#methode1
def max_profit(prices):
    max_profit=0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if max_profit<=prices[j]-prices[i]:
                max_profit=prices[j]-prices[j]
    return max_profit   






