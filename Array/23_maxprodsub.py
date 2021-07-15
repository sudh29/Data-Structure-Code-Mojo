# Maximum Product Subarray 
# Given an array Arr that contains N integers (may be positive,
#  negative or zero). Find the product of the maximum product subarray.

def maxProduct1(arr, n):
    maxtemp=arr[0]
    for i in range(n):
        temp=arr[i]
        for j in range(i+1,n):
            temp*=arr[j]
            maxtemp=max(maxtemp,temp)
        maxtemp=max(maxtemp,temp)
    return maxtemp


def maxProduct2(arr, n):
    minprod = arr[0]
    maxprod = arr[0]
    res = arr[0]
    for i in range(1, n):
        min1=minprod*arr[i]
        max1=maxprod*arr[i]
        minprod= min(arr[i],min1,max1)
        maxprod=max(arr[i],max1,min1)
        res=max(res,maxprod)
    return res
    

A = [6, -3, -10, 0, 2]
B=[8 ,-2, -2, 0 ,8 ,0, -6, -8, -6 ,-1]
C=[-8 ,5, 3, 1, 6]
print(maxProduct2(B,len(B)))
