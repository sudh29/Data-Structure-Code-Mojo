# Rearrange array in alternating positive & negative items with O(1)
# extra space

# Given an array of positive and negative numbers, arrange them in an 
# alternate fashion such that every positive number is followed by
# negative and vice-versa maintaining the order of appearance.
# Number of positive and negative numbers need not be equal. If there
# are more positive numbers they appear at the end of the array. If
# there are more negative numbers, they too appear in the end of the
# array.


def postiveNegative(arr,n):
    arr.sort()
    i=0
    while arr[i]<0:
        i+=1
    j=1
    while arr[j]<0 and j<n:    
        arr[j],arr[i]=arr[i],arr[j]
        j+=2
        i+=1
    return arr

arr1 = [1, 2, 3, -4, -1, 4]
arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

print(postiveNegative(arr2,len(arr2)))