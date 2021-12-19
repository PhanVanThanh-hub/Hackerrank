def divisibleSumPairs(n, k, ar):
    temp =0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                print(ar[i],':',ar[j])
                temp+=1
    return temp
n=6
k=3
ar=[1 ,3 ,2 ,6 ,1, 2]
print("ok:",divisibleSumPairs(n,k,ar))