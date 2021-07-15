# Given two sorted arrays arr1[] of size N and arr2[] of size M. 
# Each array is sorted in non-decreasing order. Merge the two arrays 
# into one sorted array in non-decreasing order without using any extra
#  space.

def merge( arr1, arr2, n, m): 
    i=0
    j=0
    k=n-1
    while (i<=k and j<m):
        if arr1[i]<arr2[j]:
            i+=1
        else:
            arr1[k],arr2[j]=arr2[j],arr1[k]
            j+=1
            k-=1
    arr1.sort()
    arr2.sort()
    return arr1+arr2


arr1 = [ 1, 5, 9, 10, 15, 20 ]
arr2 = [ 2, 3, 8, 13 ]
print(merge(arr1,arr2,len(arr1),len(arr2)))