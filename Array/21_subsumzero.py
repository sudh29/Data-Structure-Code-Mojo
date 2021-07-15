# Given an array of positive and negative numbers.
# Find if there is a subarray (of size at-least one) with 0 sum.

def sumzero(arr,n):
    temp=0
    for i in range(n):
        for j in range(i,n):
            temp+=arr[j]
            if temp==0:
                return True
        temp=0
    return False

def subArrayExists(arr,n):
    s=0
    temp=set()
    for i in range(n):
        s+=arr[i]
        if s in temp or s==0:
            return True
        temp.add(s)
    return False

a=[4,2,-3,1,6]
b=[4 ,2 ,0 ,1 ,6]
print(subArrayExists(b,len(b)))