# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day. You want to maximize your profit by choosing a 
# single day to buy one stock and choosing a different day in the future
#  to sell that stock. Return the maximum profit you can achieve from 
# this transaction. If you cannot achieve any profit, return 0.

def maxProfit1( prices):
    n=len(prices)
    profit=0
    for i in range(n):
        for j in range(i,n):
            profit=max(profit,prices[j]-prices[i])
    return profit

def maxProfit( prices):
    n=len(prices)
    if n==0 or n==1:
        return 0
    profit=0
    maxProfit=0
    minval=prices[0]
    for i in range(n):
        minval=min(minval,prices[i])
        profit=prices[i]-minval
        maxProfit=max(maxProfit,profit)
    return maxProfit



ll=[2,4,1]
ll1=[7,6,4,3,1]
ll2=[7,1,5,3,6,4]
ll3=[100, 180, 260, 310, 40, 535, 695];
print(maxProfit(ll))