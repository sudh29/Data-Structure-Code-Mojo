# Majority Element II
# Given an integer array of size n, find all elements that appear
# more than ⌊ n/3 ⌋ times. Follow-up: Could you solve the problem
# in linear time and in O(1) space?

def majorityElement( nums):
    n=len(nums)
    times=n//3
    res=[]
    dic={}
    for i in range(n):
        if nums[i] not in dic:
            dic[nums[i]]=1
        else:
            dic[nums[i]]+=1
    # print(dic)
    for i,j in dic.items():
        if j > times:
            res.append(i)
    return res


import sys
def majorityElement1( arr):
    n=len(arr)
    res=[]
    count1 = 0
    count2 = 0
    first = 10**12
    second = 10**12
    for i in range(0, n):
        if (first == arr[i]):
            count1 += 1
        elif (second == arr[i]):
            count2 += 1
        elif (count1 == 0):
            count1 += 1
            first = arr[i]
        elif (count2 == 0):
            count2 += 1
            second = arr[i]
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    for i in range(0, n):
        if (arr[i] == first):
            count1 += 1
        elif (arr[i] == second):
            count2 += 1
    if (count1 > n / 3):
        res.append(first)
    if (count2 > n / 3):
        res.append(second)
    return res


# ip=[3,2,3]
# ip=[1]
ip=[1,2]
print(majorityElement1(ip))