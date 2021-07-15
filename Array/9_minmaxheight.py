# Minimize the Heights II 

# Given an array arr[] denoting heights of N towers 
# and a positive integer K, you have to modify the 
# height of each tower either by increasing or 
# decreasing them by K only once. After modifying, 
# height should be a non-negative integer. 
# Find out what could be the possible minimum 
# difference of the height of shortest and longest
#  towers after you have modified each tower.


def getMinDiff( arr, n, k):
    arr.sort()
    ans=arr[-1]-arr[0]
    small=0
    big=0
    for i in range(1,n):
        if arr[i]>=k:
            small=min(arr[0]+k,arr[i]-k)
            big=max(arr[i-1]+k,arr[-1]-k)
            ans=min(ans,big-small)
    return ans


K = 2
N = 4
Arr = [1, 5, 8, 10]
print(getMinDiff(Arr,N,K))