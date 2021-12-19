
s="hhaacckkekraraannk"

def hackerrankInString(s):
    i=0
    c="hackerrank"
    while i<len(s):
        if s[i] ==  c[0]:
            c=c[1:]
        i+=1
        if c=="":
            return "YES"
    if c!="":
        return "NO"
print("ok:",hackerrankInString(s))
