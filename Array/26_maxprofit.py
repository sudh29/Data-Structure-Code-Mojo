# Best Time to Buy and Sell Stock III
# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day. Find the maximum profit you can achieve. You may
# complete at most two transactions. Note: You may not engage in
#  multiple transactions simultaneously (i.e., you must sell the 
#  stock before you buy again).

def maxProfit( prices):
    n=len(prices)
    if n==0 or n==1:
        return 0
    profit=[0]*n
    maxprice=prices[n-1]
    for i in range(n-2,0,-1):
        maxprice=max(maxprice,prices[i])
        profit[i]=max(profit[i+1],maxprice-prices[i])
    
    minprice=prices[0]
    for i in range(1,n):
        minprice=min(minprice,prices[i])
        profit[i]=max(profit[i-1],profit[i]+(prices[i]-minprice))

    return profit[n-1]


def maxProfit1( prices):
    n=len(prices)
    t1cost=2**20
    t2cost=2**20
    profit1=0
    profit2=0
    for i in range(n):
        t1cost=min(t1cost,prices[i])
        profit1=max(profit1,prices[i]-t1cost)
        t2cost= min(t2cost,prices[i]-profit1)
        profit2=max(profit2,prices[i]-t2cost)
    return profit2

# prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
prices = [1]
print(maxProfit1(prices))