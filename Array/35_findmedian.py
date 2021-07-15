# Find the median 
# Given an array arr[] of N integers, calculate the median

def find_median(v):
    n=len(v)
    v.sort()
    if n%2==0:
        return (v[n//2]+v[(n//2)-1])//2
    else:
        return v[(n//2)]
    


# N = 5
# arr = [90, 100 ,78 ,89,67]
N = 4
arr = [56, 67, 30, 79]
print(find_median(arr))