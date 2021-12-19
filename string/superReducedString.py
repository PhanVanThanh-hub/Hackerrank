def superReducedString(s):
    i=0
    x=len(s)
    while i<x-1:
        if s[i]==s[i+1]:
            s = s[:i] + s[(i + 2):]
            i=0
        else:
            i+=1
        x=len(s)
        if x<=1:
            break
    if len(s)==0:
        return "Empty String"
    return s
# tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh
# tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh
s="aaabccddd"
print("ok:",superReducedString(s))