def birthday(s, d, m):
    temp=0
    if len(s)<m:
        return 0
    if m==1 and len(s)==1:
        if s[0]==d:
            return 1
        else:
            return 0
    for i in range(0,len(s)-m+1):
        sum1=0
        for j in range(i,i+m):
            sum1+=s[j]
        if sum1==d:
            print("?:",s[i:i+m])
            temp+=1
    return temp


s=[2 ,5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d=18
m=7
print("ok:",birthday(s,d,m))