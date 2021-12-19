s='ABC'
c='d'
def numberOfDistinctString(s,c):
    def cc(s,c):
        temp=set()
        if s=="":
            return {"",c}
        for z in cc(s[1:],c):
            temp|={s[0]+z,c+s[0]+z}
        return temp
    return len(cc(s,c))
print(numberOfDistinctString(s,c))