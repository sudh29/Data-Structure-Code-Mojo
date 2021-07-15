# Implement next permutation, which rearranges numbers into the 
# lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it 
# as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

from itertools import permutations

def nextPermutation1( nums):
    plist= permutations(nums)
    plist=list(plist)
    plist.sort()
    # print(plist)
    for i in  range(len(plist)):
        if list(plist[i])==nums:
            if i==len(plist)-1:
                return list(plist[0])
            return list(plist[i+1])


def nextPermutation( nums):
    n=len(nums)
    if n==0 or n==1:
        return nums
    i=n-2
    while(i>=0 and nums[i] >=  nums[i+1]):
        i-=1
    if (i>=0):
        j=n-1
        while(nums[j]<=nums[i]):
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
    nums[i+1:]=nums[i+1:][::-1]
    return nums

    

ip=[1,1,5]
ip1=[1,2,3]
print(nextPermutation(ip1))