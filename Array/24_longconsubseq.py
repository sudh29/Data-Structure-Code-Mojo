# Longest consecutive subsequence 

# Given an array of positive integers. Find the length of the longest
#  sub-sequence such that elements in the subsequence are consecutive
#  integers, the consecutive numbers can be in any order.
 

def findLongestConseqSubseq(arr, N):
    arr.sort()
    # print(arr)
    c=0
    res=0
    for i in range(1,N):

        if arr[i]==arr[i-1]+1 :
            c+=1
            res=max(res,c)
        elif arr[i]==arr[i-1]:
            pass
        else:
            c=0
    return res+1

def findLongestConseqSubseq1(arr, N):
    A=set()
    for i in arr:
        A.add(i)
    res=0
    for i in range(N):
        if arr[i]-1 not in A:
            j=arr[i]
            while j in A:
                j+=1
            res=max(res,j-arr[i])
    return res


a=[2,6,1,9,4,5,3]
# a=[1,9,3,10,4,20,2]
# a=[6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6]
print(findLongestConseqSubseq1(a,len(a)))