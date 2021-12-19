def breakingRecords(scores):
    maxS=scores[0]
    minS=scores[0]
    maxSS=0
    minSS=0
    for i in scores:
        if i>maxS:
            maxSS+=1
            maxS=i
        if i<minS:
            minSS+=1
            minS=i
    print(maxSS,minSS)
    return True
scores=[10 ,5 ,20 ,20 ,4 ,5 ,2 ,25 ,1]
print("ok:",breakingRecords(scores))