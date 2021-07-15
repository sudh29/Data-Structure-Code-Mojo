# Cyclically rotate an array by one 

def rotate( arr, n):
    temp=arr.pop()
    arr.insert(0,temp)
    return arr

N = 5
A = [1, 2, 3, 4, 5]
print(rotate(A,N))