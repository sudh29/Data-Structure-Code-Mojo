# Given two arrays a[] and b[] of size n and n 
# respectively. The task is to find union between
# these two arrays. Union of the two arrays can be
# defined as the set containing distinct elements 
# from both the arrays. If there are repetitions, 
# then only one occurrence of element should be
# printed in union.



def doUnion(a,n,b,m):
    res=[]
    for i in range(n):
        if a[i] not in res:
            res.append(a[i])
    for j in range(m):
        if b[j] not in res:
            res.append(b[j])        
    return len(res)



n,m = 5, 3
a=[1 ,2, 3, 4, 5]
b=[1, 2, 3]

print(doUnion(a,n,b,m))