# Array Subset of another array
# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
# Task is to check whether a2[] is a subset of a1[] or not. Both 
# the arrays can be sorted or unsorted. It may be assumed that 
# elements in both array are distinct.


def isSubset( a1, a2, n, m):
    dic={}
    for i in range(n):
        if a1[i] in dic:
            dic[a1[i]]+=1
        else:
            dic[a1[i]]=1

    for i in range(m):
        if a2[i] in dic and dic[a2[i]] > 0:
            dic[a2[i]]-=1
        else:
            return "No"
    return "Yes"

a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]
# a1 = [1, 2, 3, 4, 5, 6]
# a2 = [1, 2, 4]
# a1 = [10, 5, 2, 23, 19]
# a2 = [19, 5, 3]
print(isSubset(a1,a2,len(a1),len(a2)))
