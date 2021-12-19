def clear(i,j,s):
    x=0
    x1= len(s)
    while x<x1:
        if s[x]!=i and s[x]!=j:
            s=s.replace(s[x],'')
            x-=1
        x += 1
        x1=len(s)
    return s
def perPair(s):
    temp =2
    if len(s)%2==1:
        if s[0]==s[-1]:
            temp +=1
        else:
            temp=0
            return temp
    x=len(s)-len(s)%2
    for i in range(0,x-2):
        if s[i]==s[i+2]:
            # print("s:",i,s[i],':',s[i+2])
            temp+=1
        else:
            temp=0

            break

    print("temp:",s,':',temp)
    return temp
def alternate(s):
    i=0
    x=len(s)
    a=[]
    while i<x-1:
        if s[i] != s[i + 1]:
            c=clear(s[i],s[i+1],s)
            if c not in a:
                if len(c)<=8:
                    a.append(c)
        i+=1
    print("a:",a)
    b=[]
    for i in range(0,len(a)):
        b.append(perPair(a[i]))
    print("b:",b)
    if not b:
        return 0
    return max(b)
s="asdcbsdcagfsdbgdfanfghbsfdab"
print("ok:",alternate(s))