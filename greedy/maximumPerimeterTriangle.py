def checkEdge(a,b,c):
    if a < b + c and  b < a + c and c < a + b:
        return True
    return False
def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    print(sticks)
    for i in range(0,len(sticks)-2):
        for j in range(i+1,len(sticks)-1,):
            for z  in range(j+1,len(sticks)):
                print(':',sticks[i],sticks[j],sticks[z])
                if checkEdge(sticks[i],sticks[j],sticks[z]):
                    return sticks[z],sticks[j],sticks[i]
    return True

sticks=[1 ,2,3]
print("ok:",maximumPerimeterTriangle(sticks))