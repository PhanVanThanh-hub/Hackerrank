n = 203
l = 20
r = 24
import numpy as np

def sumOfOnes(n,l,r):
    arr = [n]
    x= len(arr)
    temp=0
    while temp!=x:
        temp=0
        for i in range(0,x):
            if arr[i]>1:
                b=arr[i]
                arr[i]=arr[i]//2
                arr.insert(i+1,b%2)
                arr.insert(i+2,b//2)
            temp+=1
        x= len(arr)
        if x==15:
            a=0
            for i in range(0,x):
                if arr[i] % 2==0:
                    a=1
            if a==0:
                return r+1-l
        print(arr, 'len:', x, ':')
    temp1=0
    print(arr, 'len:', x, ':')
    k=0
    for i in range(l-1,r):
        if arr[i]==1:
            temp1 +=1
    while r % 2 == 0:
        k +=1
        r /= 2
    r1 = (r + pow(2, k)) / pow(2, k + 1)
    print(r,k,r1)

    return temp1



print('lmao',sumOfOnes(n,l,r))