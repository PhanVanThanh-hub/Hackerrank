def saveThePrisoner(n, m, s):
    print(m//n,':',m%n)

    return (m+s-2)%n+1


n=12
m=430895283
s=10
print("ok:",saveThePrisoner(n,m,s))