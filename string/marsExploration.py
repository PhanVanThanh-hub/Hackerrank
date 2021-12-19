s="QQQ"
def marsExploration(s):
    temp =0
    for i in range(0,len(s),3):

        if(s[i]!="S"):
            temp+=1
        if (s[i+1] != "O"):
            temp += 1
        if (s[i+2] != "S"):
            temp += 1
    return temp

print("ok:",marsExploration(s))

