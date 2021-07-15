# Given an array of N integers, and an integer K, find the number
#  of pairs of elements in the array whose sum is equal to K.


def getPairsCount(arr,n,k):
    c=0
    di={}
    for i in range(n):
        if arr[i] not in di:
            di[arr[i]] = 1
        else:
            di[arr[i]]+=1
    for j in range(n):
        if (k-arr[j]) in di:
            c += di[k-arr[j]]
        if (k-arr[j])== arr[j]:
            c-=1
    return c//2


# a,n,k=[1,5,7,1],4,6
a,n,k=[1,1,1,1],4,2
print(getPairsCount(a,n,k))