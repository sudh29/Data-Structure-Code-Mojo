# Given an array of N integers arr[] where each element represents 
# the max number of steps that can be made forward from that element.
#  Find the minimum number of jumps to reach the end of the array 
# (starting from the first element). If an element is 0, then you 
# cannot move through that element.


def minJumps( arr, n):
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    jumps=1
    step=arr[0]
    maxreach=arr[0]
    for i in range(1,n):
        if (i==n-1):
            return jumps
        maxreach= max(maxreach,i+arr[i])
        step-=1
        if step==0:
            jumps+=1
            if i>=maxreach:
                return -1
            step=maxreach-i
    return -1

N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr,N)) 