def jumpingOnClouds(c, k):
    e=100
    i=0
    while (i+k)%len(c)!=0:
        i=(i+k)%len(c)
        e -=1

        if c[i]==1:
            e-=2
        print("i:", i, ':', c[i], ':', e)
    if c[0]==1:
        return e-3
    return e-1




k = 3
c = [1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0]
print("ok:",jumpingOnClouds(c,k))