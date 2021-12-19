def flatlandSpaceStations(n, c):
    c.sort()
    if n==len(c):
        return 0
    # a = []
    # for i in range(0, n):
    #     b = []
    #     for j in c:
    #         if len(b) != 0:
    #             if abs(i - j) < min(b):
    #                 b.append(abs(i - j))
    #             else:
    #                 break
    #         else:
    #             b.append(abs(i - j))
    #     a.append(min(b))
    #
    # return max(a)
    a=[]
    if len(c)<2:
        return max(c[0]-0,abs(0-n-1))
    for i in range(0,n):
        print(a,':',c)
        b=[]
        j=0
        b.append(abs(i-c[j]))
        b.append(abs(i-c[j+1]))
        if i>c[j] and i==c[j+1] and len(c)>2:
            c.remove(c[j])
        a.append(min(b))
    print(a)
    return True
n=100
c = [99]
print("ok:",flatlandSpaceStations(n,c))