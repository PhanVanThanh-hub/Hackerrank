def funnyString(s):
    print('a:',s[::-1])
    x= len(s)-1
    for i  in range(0,len(s)//2):
        print(":",ord(s[x]) )
        if abs(ord(s[i])-ord(s[i+1]))!=abs(ord(s[x-i])-ord(s[x-i-1])):
            return "Not Funny"


    return "Funny"

s="acxz"
print("ok:",funnyString(s))