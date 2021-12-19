def extraLongFactorials(n):
    temp=1
    for i in range(n,1,-1):
        temp *=i
        print("temp:",temp)
    return temp

n=45
print("ok:",extraLongFactorials(n))