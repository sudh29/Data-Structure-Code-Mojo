# Chocolate Distribution Problem 
# Given an array A[ ] of positive integers of size N, where each 
# value represents the number of chocolates in a packet. Each packet 
# can have a variable number of chocolates. There are M students, the
# task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a
# student and minimum number of chocolates given to a student
# is minimum.


def findMinDiff(A,N,M):
    A.sort()
    # print(A)
    mindiff=2**20
    for i in range(N-M+1):
        # print(A[i+M-1],A[i])
        diff= A[i+M-1]-A[i]
        mindiff=min(diff,mindiff)
    return mindiff
    

N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]
print(findMinDiff(A,N,M))