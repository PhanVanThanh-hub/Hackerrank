def permutationEquation(p):
    # Write your code here
    p.insert(0,0)
    for i in range(1,len(p)):
        print("??????:",i)
        for j in range(0,len(p)):
            if p[j]==i:
                for z in range(0,len(p)):
                    if j==p[z]:
                       print("?:",i,':',p[j],':',j,':',p[z],':',z)
    return True

p=[4 ,3, 5, 1, 2]
print("ok:",permutationEquation(p))