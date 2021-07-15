# Given an array of integers. Find the Inversion Count in the array.
# Inversion Count: For an array, inversion count indicates how far 
# (or close) the array is from being sorted. If array is already 
# sorted then the inversion count is 0. If an array is sorted in 
# the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if 
# a[i] > a[j] and i < j.

# IMP

def merge(arr,temp,left,right):
    c=0
    if left<right:
        mid=(left+right)//2
        c+=merge(arr,temp,left,mid)
        c+=merge(arr,temp,mid+1,right)
        c+=mergesort(arr,temp,left,mid,right)
    return c

def mergesort(arr,temp,left,mid,right):
    i=left
    j=mid+1
    k=left
    c=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            c+=(mid-i+1)
            k+=1
            j+=1
    while i<= mid:
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<=right:
        temp[k]=arr[j]
        k+=1
        j+=1
    for m in range(left,right+1):
        arr[m]=temp[m]
    return c

def inversionCount( arr, n):
    temp=[0]*n
    return merge(arr,temp,0,n-1)


arr = [2, 4, 1, 3, 5]
print(inversionCount(arr,5))