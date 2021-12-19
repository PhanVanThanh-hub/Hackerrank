
def commonChild(s1, s2):
    # x1=len(s1)
    # x2=len(s2)
    # z1=[]
    # z2=[]
    # for i in range(0,x1):
    #     j=0
    #     while j<x2:
    #         if s1[i]==s2[j]:
    #             z1.append(s1[i])
    #             x2=len(s2)
    #             if i>=j:
    #                 print("j:",j,':',s1[i],':',len(z2))
    #                 if s1[i] in z2 and i<len(s2):
    #                     break
    #                 z2.insert(j, s1[i])
    #                 j=0
    #                 break
    #             break
    #         j += 1
    #         x2=len(s2)
    # print("s1:",z1)
    # print("s2:", z2)
    # d=[]
    # if not z1 or not z2:
    #     return 0
    # for i in range(0,len(z1)-1):
    #     a=""
    #     x=i
    #     for j in range(0,len(z2)-1):
    #         if z1[x]==z2[j]:
    #             a +=z1[x]
    #             x+=1
    #         elif a!="":
    #             d.append(a)
    #             break
    #         if j==len(z2)-1 or x>len(z1)-1:
    #             d.append(a)
    #             break
    # print("D:",d)
    # print(len(max(d,key=len)))
    # return len(max(d,key=len))

    x1=len(s1)
    x2 = len(s2)
    z1=[]
    for i in range(0, x1):
        j=0
        while j<x2:
            if s1[i]==s2[j]:
                z1.append(s1[i])
                x2=len(s2)
                break
            j += 1
    print("a:",z1)
    i=0
    x11=len(z1)

    d=[]
    while i<x11-1:
        a=""
        j=0
        p=i
        while j<x2-1:
            if z1[p]==s2[j]:
                a+=z1[p]
                p+=1
            j+=1
            if p==x11-1:
                break
        d.append(a)
        i+=1
    print("D:",d)
    print("?:",max(d,key=len))

s1="ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP"
s2="FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX"
print("OK:",commonChild(s1,s2))

as1="07:05:45PM"
s="00"+as1[2:len(as1)-2]
print("as:",s[0])
s="12"
zz=int(s[:2])+12
print(str(zz))
