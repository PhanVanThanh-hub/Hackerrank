from struct import Struct

s=[98,14,70,19,59,17,27,27,22,92,10,0,75,28,23,12,47,51,50,81]

e=[139,32,93,44,78,65,61,29,115,107,41,84,98,68,32,85,75,81,123,151]

temp = 0
m=[s[0]]
n=[e[0]]
cl={}
for i in range(len(s)):
    cl['s[i]'].append(e[i])
print(cl)
for i in range(0,len(s)):
    print("",e[i]-s[i])
    temp = 0
    for a in range(0,len(m)):
        if (s[i]<=m[a] and e[i]<m[a])or (s[i]>=n[a]) or e[i]<=m[a]:
            temp=1
        else:

            temp=0
            break


    if temp== 1:
        m.append(s[i])
        n.append(e[i])
print(m)
print(len(m))