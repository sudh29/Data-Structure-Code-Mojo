# Three way partitioning 
# Given an array of size n and a range [a, b]. The task is to partition
# the array around the range such that array is divided into three 
# parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order.
# You are required to return the modified array.


def threeWayPartition( array, a, b):
    n=len(array)
    start=0
    end=n-1
    i=0
    while i<=end:

        if array[i]<a:
            array[i],array[start]=array[start],array[i]
            i+=1
            start+=1
        elif array[i]>b:
            array[i],array[end]=array[end],array[i]
            end-=1
        else:
            i+=1
    return array

n=4
A=[87, 78, 16, 94]
a,b=36, 72
print(threeWayPartition(A,a,b))