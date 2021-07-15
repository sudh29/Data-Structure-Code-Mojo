# Triplet Sum in Array
# Given an array arr of size n and an integer X. Find if there's a 
# triplet in the array which sums up to the given integer X.


def find3Numbers(A, n, X):
    for i in range(n):
        temp=X-A[i]
        for j in range(i+1,n):
            temp2=temp-A[j]
            for k in range(j+1,n):
                if temp2==A[k]:
                    return 1
    return 0



def find3Numbers1(A, n, X):
    A.sort()
    for i in range(n-2):
        j=i+1
        k=n-1
        while j<k:
            if A[i]+A[j]+A[k]==X:
                    return 1
            elif A[i]+A[j]+A[k] < X:
                j+=1
            else:
                k-=1
    return 0



# n = 6
# X = 13
# arr = [1, 4, 45, 6, 10, 8]
n = 5
X = 20
arr = [1, 2, 4, 3, 6]

print(find3Numbers1(arr,n,X))