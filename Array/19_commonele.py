# Given three arrays sorted in increasing order. Find the elements that
# are common in all three arrays. Note: can you take care of the 
# duplicates without using any additional Data Structure?

def commonElements(A, B, C, n1, n2, n3):
    m1={}
    m2={}
    m3={}
    temp=[]
    for i in range(n1):
        if A[i] not in m1:
            m1[A[i]] = 1
        else:
            m1[A[i]]+=1
    for i in range(n2):
        if B[i] not in m2:
            m2[B[i]] = 1
        else:
            m2[B[i]]+=1
    for i in range(n3):
        if C[i] not in m3:
            m3[C[i]] = 1
        else:
            m3[C[i]]+=1

    for i in range(n1):
        if A[i] in  m1 and A[i] in m2 and A[i] in m3 :
            if m1[A[i]]>0 and m2[A[i]]>0 and m3[A[i]]>0:
                temp.append(A[i])
            m1[A[i]]=0
 
    return temp

def commonElements1(ar1, ar2, ar3, n1, n2, n3):
    i, j, k = 0, 0, 0 
    temp=[]
    while (i < n1 and j < n2 and k< n3):
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            temp.append( ar1[i])
            i += 1
            j += 1
            k += 1
        elif ar1[i] < ar2[j]:
            i += 1             
        elif ar2[j] < ar3[k]:
            j += 1   
        else:
            k += 1
    return temp

n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(commonElements1(A, B, C, n1, n2, n3))