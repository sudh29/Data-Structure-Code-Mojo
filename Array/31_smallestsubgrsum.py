# Smallest subarray with sum greater than a given value

def smallestsub(arr,x):
    n=len(arr)
    mlen=n+1
    for i in range(n):
        temp=arr[i]
        if temp>x:
            return 1
        for j in range(i+1,n):
            temp+=arr[j]
            if temp>x and j-i+1 < mlen:
                mlen=j-i+1
    return mlen

def smallestsub1(arr,x):
    n=len(arr)
    mlen=n+1
    temp=0
    i=0
    j=0
    while j < n:
        while temp<=x and j<n:
            temp+=arr[j]
            j+=1
        while temp>x and i<n:
            if j-i < mlen:
                mlen=j-i
            temp-=arr[i]
            i+=1
    return mlen


arr = [1, 4, 45, 6, 0, 19]
x  =  51
# arr = [1, 10, 5, 2, 7]
# x  = 9
# arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
# x = 280
# arr = [1, 2, 4]
# x = 8
print(smallestsub(arr,x))