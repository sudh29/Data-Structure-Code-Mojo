# Move all negative numbers to beginning and 
# positive to end with constant extra space

def neg(arr):
    j=0
    for i in range(len(arr)):
        if arr[i] <0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr



a=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
print(neg(a))