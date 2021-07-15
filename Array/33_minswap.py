# Minimum swaps and K together

# Given an array of n positive integers and a number k. 
# Find the minimum number of swaps required to bring all the numbers 
# less than or equal to k together.

def minSwap (arr, n, k) : 
    cnt=0
    for i in range(n):
        if arr[i]<=k:
            cnt+=1
    bad=0
    for i in range(cnt):
        if arr[i]>k:
            bad+=1
    minstep=bad
    j=cnt
    for i in range(n):
        if j==n:
            break
        if arr[i]>k:
            bad-=1
        if arr[j]>k:
            bad+=1
        minstep=min(minstep,bad)
        j+=1
    return minstep


# arr = [2, 1, 5, 6, 3] 
# K = 3
arr = [2, 7, 9, 5, 8, 7, 4] 
K = 6
print(minSwap(arr,len(arr),K))