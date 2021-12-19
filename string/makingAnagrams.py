#https://www.hackerrank.com/challenges/making-anagrams/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def makingAnagrams(s1, s2):
    newS1=list(s1)
    newS2=list(s2)
    index=0
    for i in newS1:
        if i in newS2:
            print("i:",i)
            index+=1
            newS2.remove(i)

    print("s",newS2)
    return len(newS1)-index+len(newS2)

s1="cde"
s2="abc"
print("hehe:",makingAnagrams(s1,s2))