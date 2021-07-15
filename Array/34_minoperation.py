# Make Array Palindrome
# For a given array, we need to make an array palindrome. 
# The only allowed operation on the array is merging the elements.
# To merge two adjacent elements just simply replace them with 
# their sum. The task is to find a minimum number of merge operations
# to make a given array palindrome.



def pal(arr,n):
    res=0
    i=0
    j=n-1
    while i<=j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        elif arr[i]>arr[j]:
            j-=1
            arr[j]+=arr[j+1]
            res+=1
        else:
            i+=1
            arr[i]=arr[i-1]
            res+=1
    return res

# n=4
# a=[10,99,44,10]
n=3
a=[20,999,20]
print(pal(a,n))