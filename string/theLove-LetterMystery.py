def theLoveLetterMystery(s):
    x=len(s)//2
    temp=0
    for i in range(0,x):
        print(s[i],':',s[-i-1],':',ord(s[i]),':',ord(s[-i-1]))
        if ord(s[i])>ord(s[-i-1]):
            print("?")
            temp+= ord(s[i])-ord(s[-i-1])
        else:
            print("!")
            temp += ord(s[-i-1]) - ord(s[i])
        print("d:",temp)
    print("zx:",temp)
    return temp
s="abc"
print("ok:",theLoveLetterMystery(s))