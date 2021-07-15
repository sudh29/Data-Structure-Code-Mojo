# Maximum and minimum of an array using minimum number of comparisons


def minmax(arr):
    mi=min(arr)
    ma=max(arr)
    return mi,ma


def minmax2(low,high,arr):
    mi=arr[low]
    ma=arr[low]
    if low==high:
        mi=arr[low]
        ma=arr[low]
        return mi,ma
    elif high==low+1:
        if arr[low]>arr[high]:
            ma=arr[low]
            mi=arr[high]
        else:
            ma=arr[high]
            mi=arr[low]
        return mi,ma
    else:
        mid=int((low+high)/2)
        mi1,ma1=minmax2(low,mid,arr)
        mi2,ma2=minmax2(mid,high,arr)
    return (min(mi1,mi2),max(ma1,ma2))

def minmax3(arr):
    n=len(arr)
    if n%2==0:
        ma=max(arr[0],arr[1])
        mi =min(arr[0],arr[1])
        i=2
    else:
        ma=mi=arr[0]
        i=1
    while(i < n-1):
        if arr[i] < arr[i+1]:
            ma=max(ma,arr[i+1])
            mi=min(mi,arr[i])
        else:
            ma=max(ma,arr[i])
            mi=min(mi,arr[i+1])
        i+=2
    return mi,ma


a=[1,2,4,-1,10]
print(minmax(a))
print(minmax2(0,len(a)-1,a))
print(minmax3(a))