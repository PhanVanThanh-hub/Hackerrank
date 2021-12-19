def alternatingCharacters(s):
    temp=0
    i=0

    while i<len(s)-1:
        if s[i]==s[i+1]:
            temp+=1
        i+=1
    return temp

s="A"
print("ok:",alternatingCharacters(s))