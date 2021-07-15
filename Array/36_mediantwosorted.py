# Median of two sorted arrays of different sizes
# Given two sorted arrays, a[] and b[], the task is to find the
# median of these sorted arrays, in O(log n + log m) time complexity,
# when n is the number of elements in the first array, and m is the 
# number of elements in the second array.
# This is an extension of median of two sorted arrays of equal size 
# problem. Here we handle arrays of unequal size also. 


def twosortedmedian(arr1,arr2):
    v=ar1+ar2
    n=len(v)
    v.sort()
    if n%2==0:
        return (v[n//2]+v[(n//2)-1])//2
    else:
        return v[(n//2)]
    
def twosortedmedian1(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    arr=[0]*(n1+n2)
    i=0
    j=0
    k=0
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j] :
            arr[k]=arr1[i]
            i+=1
            k+=1
        else :
            arr[k]=arr2[j]
            j+=1
            k+=1
    while i<n1:
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j <n2:
        arr[k]=arr2[j]
        j+=1
        k+=1
    n=len(arr)
    if n%2==0:
        return (arr[n//2]+arr[(n//2)-1])//2
    else:
        return arr[(n//2)]

        

ar1 = [-5, 3, 6, 12, 15]
ar2 = [-12, -10, -6, -3, 4, 10]
print(twosortedmedian1(ar1,ar2))