# Kadane's Algorithm 
# Given an array arr of N integers. 
# Find the contiguous sub-array with maximum sum.

def maxSubArraySum(a,size):
    maxsum= -3200
    temp=0
    for i in range(size):
        temp+=a[i]
        if maxsum<temp:
            maxsum=temp
        if temp<0:
            temp=0
    return maxsum


A=[1,2,3,-2,5]
print(maxSubArraySum(A,len(A)))