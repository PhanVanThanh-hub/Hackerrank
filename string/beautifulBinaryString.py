def beautifulBinaryString(b):
    temp = 0
    i=0
    while i<len(b)-2:
        # print("b:",b[i],':',i)
        if b[i]=="0" and b[i+2]=="0":
            if b[i+1]=="1":
                temp+=1
                i +=2
        i+=1
    return temp

b="0101010"
print("ok:",beautifulBinaryString(b))