import re
from itertools import combinations


def pairing(s):
    temp=0
    c=s
    i=0
    x1=len(c)
    z=[]
    while i<x1:
        if re.search("[a-z]", c[i]):
            temp +=1
            z.append(c[i])
            c=c.replace(c[i],'')
        x1=len(c)
    z.sort()
    print("Z:",z)
    if len(z)<=1:
        return 0
    return z
def alternate(s):
    if len(s)<2:
        return 0
    st=pairing(s)#lấy số lượng kí tự xuất hiện trong chuỗi s .Có thể thay thế =list(combinations(st,len(st)-2))
    if st==0:
        return 0
    a = list(combinations(st, len(st) - 2)) #chọn tổ hợp (hoán vị) từ n->n-2 số
    print(len(a))
    b=[]
    for i in a:
        s1=s
        for j in i:
            s1 = s1.replace(j, '')
        x= len(s1)
        temp=2
        if len(s1) % 2 == 1: #check xem chiều dài chuỗi là chẵn hay lẻ
            if s1[0] == s1[-1]:#nếu chuổi chẵn thì kí tự đầu và kí tự cuối giống nhau
                temp += 1
            else:
                temp=0
                continue

        x = len(s1) - len(s1) % 2# loại kí tự cuối nếu như độ dài chuỗi lẻ
        for i in range(0, x - 2):
            if s1[i] == s1[i + 2]:
                temp += 1
            else:
                temp = 0
                break
        b.append(temp)
    if not b:
        return 0

    return max(b)

s="tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi"

print(":",alternate(s))