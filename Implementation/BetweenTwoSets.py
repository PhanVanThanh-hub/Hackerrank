def getTotalX(a, b):
    c=[]
    i = 0
    while True:#liệt kê các số nằm trong khoảng
        z=0
        z=b[0]-a[-1]*i
        if z<a[-1]:
            break
        c.append(z)
        i+=1
    i=0
    az=len(c)
    while i<az:
        for j in a:
            if j>=c[i]:
                if j%c[i]!=0:

                    c.remove(c[i])
                    i-=1

                    break
            elif c[i]%j!=0:

                c.remove(c[i])
                i-=1
                break
        i+=1
        az=len(c)
    i=0
    while i < az - 1:
        for j in b:
            if j > c[i]:
                if j % c[i] != 0:

                    c.remove(c[i])
                    i -= 1
                    break
            elif c[i] % j != 0:

                c.remove(c[i])
                i -= 1
                break
        i += 1
        az = len(c)
    print("c:",c)
    return(len(c))

a=[2,4]
b=[16,32 ,96]
print("ok:",getTotalX(a,b))