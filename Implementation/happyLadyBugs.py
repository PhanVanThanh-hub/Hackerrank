def happyLadybugs(b):
    # Write your code here
    i = 0
    b1 = b.replace("_", '')
    x = len(b1)
    while x > 0:
        temp = 0
        for j in range(0, x):
            if b1[i] == b1[j]:
                temp += 1

        if temp == 1:
            return "NO"
        b1 = b1.replace(b1[i], '')
        x = len(b1)

    temp=0
    for i in range(0,len(b)):
        if b[i]=="_":
            temp=1
            break
    if temp==0:
        for i in range(0,len(b)-1):
            if i !=0 :
                if (b[i]==b[i-1] or b[i]==b[i+1]):
                    continue
                else:
                    return "NO"
            if b[i]!=b[i+1]:
                return "NO"
        print("?")
        return "YES"

    return "YES"



b="AABCBC"
print("ok:",happyLadybugs(b))