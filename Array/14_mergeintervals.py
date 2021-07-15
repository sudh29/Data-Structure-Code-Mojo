# Given an array of intervals where intervals[i] = [starti, endi],
#  merge all overlapping intervals, and return an array of the
#  non-overlapping intervals that cover all the intervals in the input.

def merge( intervals):
    intervals.sort()
    n=len(intervals)
    res=[]
    temp=-32000
    tmax=-32000
    for i in range(n):
        if intervals[i][0]>tmax:
            if i!=0:
                res.append([temp,tmax])
            tmax=intervals[i][1]
            temp=intervals[i][0]
        else:
            if intervals[i][1]>tmax:
                tmax=intervals[i][1]
    if tmax != -32000  and [temp,tmax] not in res:
        res.append([temp,tmax])
    return res



I=[[1,3],[2,6],[8,10],[15,18]]
I1=[[1,4],[4,5]]
print(merge(I))