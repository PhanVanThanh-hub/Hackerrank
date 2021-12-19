def serviceLane(n, cases):
    a=[]
    for i in cases:
        min=-1
        print("",i)
        for j in range(i[0],i[1]+1):
            print(width[j],': ',end="")
            if width[j]<min or min==-1:
                min=width[j]
        a.append(min)
        print(min)


    return a
n=8
width = [1 ,2 ,2 ,2 ,1]
cases = [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]
print("ok:",serviceLane(n,cases))