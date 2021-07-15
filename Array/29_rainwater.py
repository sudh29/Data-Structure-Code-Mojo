# Trapping Rain Water 
# Given an array arr[] of N non-negative integers representing the 
# height of blocks. If width of each block is 1, compute how much
#  water can be trapped between the blocks during the rainy season. 

def trappingWater(arr,n):
    left=[0]*n
    right=[0]*n
    res=0

    left[0]=arr[0]
    for j in range(1,n):
        left[j]=max(left[j-1],arr[j])

    right[n-1]=arr[n-1]
    for j in range(n-2,-1,-1):
        right[j]=max(right[j+1],arr[j])
    
    for i in range(n):
        res+=min(left[i],right[i])-arr[i]
    return res

# N = 6
# arr= [3,0,0,2,0,4]
# N = 4
# arr = [7,4,0,9]
# N = 3
# arr = [6,9,9]
N=7
arr=[8, 8, 2, 4, 5, 5, 1]
print(trappingWater(arr,N))