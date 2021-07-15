# Given an array of integers nums containing n + 1 integers where each
#  integer is in the range [1, n] inclusive. There is only one repeated 
# number in nums, return this repeated number. You must solve the 
# problem without modifying the array nums and uses only constant
#  extra space.


def findDuplicate( nums):
    n=len(nums)
    arr=[0]*n
    for i in nums:
        if arr[i-1]==1:
            return i
        else:
            arr[i-1]=1

def findDuplicate2( nums):
    hare = nums[0]
    tortoise = nums[0]
    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        if hare == tortoise:
           break
    ptr = nums[0]
    while ptr!=tortoise:
        ptr = nums[ptr]
        tortoise = nums[tortoise]
    return ptr
                
nums = [1,3,4,2,2]
print(findDuplicate2(nums))



from collections import Counter
 
l1 = [1,3,4,2,2]
d = Counter(l1)
new_list = list([item for item in d if d[item]>1])
# print(new_list)
