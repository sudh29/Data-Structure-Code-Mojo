# Factorials of large numbers
import sys

tempcache={}
def factorial(n):
    if n in tempcache:
        return tempcache[n]
    if n==1 or n==0:
        val=  1
    else: 
        val= n*factorial(n-1)
    tempcache[n]=val
    return val

def mul(x,res,size):
    c=0
    i=0
    while i < size:
        p = res[i]*x + c
        res[i]= p%10
        c=p//10
        i+=1
    while c:
        res[size]=(c%10)
        c=c//10
        size+=1
    return size

def fact(n):
    res=[None]*5000
    res[0]=1
    s=1
    for i in range(2,n+1):
        s= mul(i,res,s)
    indx= (res.index(None))
    res= (res[0:indx])
    res.reverse()
    return res




n=10
print(fact(n))