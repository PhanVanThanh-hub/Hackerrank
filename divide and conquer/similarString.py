
def similarStrings(a,b):
    print(a,b)
    if len(a)==1 and a!=b:
        return False
    if a==b:
        return True
    elif len(a) %2==0:
        a1=a[0:(len(a)//2)]
        a2=a[len(a)//2:len(a)]
        b1=b[0:len(b)//2]
        b2=b[len(b)//2:len(b)]
        # similarStrings(a1,b1)
        # similarStrings(a2, b2)
        # similarStrings(a1, b2)
        # similarStrings(a2, b1)
        if (a1==b1 and a2==b2) or (a1==b2 and a2==b1):
            return True
    else:
        return False

a="aabb"
b="abaa"
print("a:",similarStrings(a,b))
