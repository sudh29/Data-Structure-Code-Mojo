# Given an array of size N containing only 0s, 
# 1s, and 2s; sort the array in ascending order.


def sort012(arr):
 # code here
    c0=arr.count(0)
    c1=arr.count(1)
    c2=arr.count(2)
    i=0
    while c0>0:
        arr[i]=0
        i+=1
        c0-=1
    while c1>0:
        arr[i]=1
        i+=1
        c1-=1
    while c2>0:
        arr[i]=2
        i+=1
        c2-=1
    return arr


a=[0,2,1,2,0]
print(sort012(a))