def utopianTree(n):
    if n==0:
        return 1
    if n==1:
        return 2
    temp=2
    for i in range(2,n+1):
        if i%2!=0:
            temp=temp*2
        else:
            temp+=1
        print("tmep:",i,':',temp)
    return temp

n=4
print("ok:",utopianTree(n))