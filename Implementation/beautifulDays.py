def beautifulDays(i, j, k):
    temp=0

    for x in range(i,j+1):
        c=0
        b=x
        while x/10!=0:
            c=c*10+x%10
            x=x//10
        if abs(c-b)%k==0:
            temp+=1

    return temp
i=20
j=23
k=6
print("ok:",beautifulDays(i,j,k))