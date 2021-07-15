# Kth smallest element 


def kthSmallest(arr, l, r, k):
    for i in range(k-1):
        mi=min(arr)
        arr.remove(mi)
    return min(arr)


a=[7, 10, 4, 3, 20, 15]
print(kthSmallest(a,1,6,3))