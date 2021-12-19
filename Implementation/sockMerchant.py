def sockMerchant(n, ar):
    a=list(set(ar))
    temp=0
    print("a:",a)
    for i in a:
        c=ar.count(i)
        print(i,':',c,':',temp)

        temp+=(c//2)
    return temp
n=1
ar=[10 ,20 ,20 ,10 ,10 ,30 ,50, 10, 20]
print("oj:",sockMerchant(n,ar))