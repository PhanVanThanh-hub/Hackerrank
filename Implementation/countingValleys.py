def countingValleys(steps, path):
    # Write your code here
    temp=0
    count1=0
    a=1
    for i in range(0,len(path)):
        if path[i]=="U":
            temp+=1
        else :
            temp-=1
        if temp>=0:
            a=1
        if temp<0 and a==1 :
            count1+=1
            a=-1

    print("coL:",count1)
    return temp
steps=8
path="UDDDUDUUDDUU"
print("ok:",countingValleys(steps,path))