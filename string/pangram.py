s="We promptly judged antique ivory buckles for the prize"
def pangrams(s):
    s=s.lower()
    a="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(s)):
        j=0
        while j<len(a):
            if s[i]==a[j]:
                a=a.translate ({ ord (a[j]): None })
                break
            j +=1

    if a=="":
        return "pangram"
    return "not pangram"



print("ok:",pangrams(s))