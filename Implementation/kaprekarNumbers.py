import  math
def checkKap(x):
    a=x
    x=int(math.pow(x,2))
    print("x:", x)
    if x==1:
        return True
    z=str(x)
    if len(z)==1:
        return False
    print(z[:len(z)//2],':',z[len(z)//2:len(z)])
    x1=int(z[:len(z)//2])
    x2=int(z[len(z)//2:len(z)])
    if x1+x2==a:
        return True
    return False
def kaprekarNumbers(p, q):
    # Write your code here
    a=[]
    for i in range(p,q+1):
        if checkKap(i):
            a.append(i)
    return a

p=400
q=700
print("ok:",kaprekarNumbers(p,q))