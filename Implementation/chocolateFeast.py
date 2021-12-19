def chocolateFeast(n, c, m):
    wrappers=n//c
    temp=wrappers

    while wrappers>=m:
        temp+=wrappers//m
        wrappers=wrappers%m+wrappers//m

    return temp

n=15
c=3
m=2
print("ok:",chocolateFeast(n,c,m))