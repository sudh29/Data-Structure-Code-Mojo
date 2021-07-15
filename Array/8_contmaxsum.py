# Kadane's Algorithm 
# Given an array arr of N integers. Find the 
# contiguous sub-array with maximum sum.

def maxSubArraySum(a,size):
    tempmax=a[0]
    temp=0
    for i in range(size):
        temp+=a[i]
        if tempmax<temp:
            tempmax=temp
        if temp<0:
            temp=0
    return tempmax


N = 5
arr = [1,2,3,-2,5]
print(maxSubArraySum(arr,N))