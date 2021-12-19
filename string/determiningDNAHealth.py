def determiningDNAHealth(g,h):
    c=[]
    for i in range(0,len(g)):
        a=[]
        a.append(g[i])
        a.append(h[i])
        c.append(a)
    print("c:",c)
    return True

g=["a" ,"b" ,"c" ,"aa", "d","b"]
h=[1,2,3,4,5,6]
print("ok:",determiningDNAHealth(g,h))