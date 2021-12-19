#https://www.hackerrank.com/challenges/anagram/problem?h_r=next-challenge&h_v=zen

def anagram(s):
    print("le:",len(s)//2)
    if(len(s)%2)!=0:
        return -1
    index=0
    newS= list(s[len(s)//2:])
    print("new:",newS)
    for i in range(len(s)//2):
        print("s:",s[i])
        if s[i] in newS:
            newS.remove(s[i])
            print("news:",newS)
            index+=1
    return len(newS)


s="fdhlvosfpafhalll"
print("hehe:",anagram(s))