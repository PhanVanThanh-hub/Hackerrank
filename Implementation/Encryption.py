import  math
import textwrap


def encryption(s):
    # Write your code here
    s=s.replace(' ','')
    x=len(s)
    a=math.sqrt(x)
    a=int(a)
    b=int(a)+1
    print(a, b,len(s))

    if a*b<len(s):
        a=b
    if len(s)//a<b and a*a>=len(s):
        print("?")

        b=a
    print(a, b, len(s))
    c=[]
    j=1

    for i in range(0,a):
        c.append(s[b*j-b:b*j])

        j+=1
    d=""
    print(c)
    for i in range(0,b):

        for j in range(0,a):

            try:
                d+=str(c[j])[i]
            except:
                continue
        d+=" "
    print(d)
    return c

s="feedthedog"
print("ok:",encryption(s))