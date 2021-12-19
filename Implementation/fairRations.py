def fairRations(B):
    temp=0
    for i in B:
        if i%2!=0:
            temp+=1
    if temp==1  :
        return "NO"
    if temp==0:
        return "0"
    amount=0
    for i in range(0,len(B)-1):
        if B[i]%2!=0:
            B[i]+=1
            B[i+1]+=1
            amount+=2
    if B[-1]%2!=0:
        return "NO"
    print(B,':',amount)
    return amount

B = [2, 3, 4, 5, 6]
print("ok:",fairRations(B))