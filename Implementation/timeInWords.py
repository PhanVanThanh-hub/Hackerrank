def text1(s):
    switcher = {
        1: 'one',
        2: '-two',
        3: 'three',
        4: 'four',
        5:'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9:'nine',
        10:'ten',
        11:'eleven'
    }
    return switcher.get(s)
def textWith1(s):
    switcher = {
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    return switcher.get(s)

def timeInWords(h, m):
    temp=0
    if m!=30:
        if m>30:
            m=60-m
            h+=1
            temp=1
            s = "to "
        else:
            s="past "
    if m==0:
        return text1(h)+" o' clock"
    if m<=10  :
        if temp==1:
            return text1(m)+ " minutes "+s + text1(h)
        return text1(m) + " minute " + s + text1(h)
    if m%15==0:
        if m==30:
            return "half past "+text1(h)
        elif m==15:
            return "quarter "+s+text1(h)
        # return "quarter to "+text1(h+1)
    if m<30:
        if m<20:
            return textWith1(m) +" minutes "+s+text1(h)
        if m==20:
            return "twenty minutes "+s+text1(h)
        return "twenty " + text1(m%10) +" minutes "+s+text1(h)
    # else:
    #     m=60-m
    #     if m <= 10 and m != 15:
    #         return text1(m) + " minute to " + text1(h+1)
    #     if m<20:
    #         return textWith1(m) +" minutes to "+text1(h+1)
    #     if m==20:
    #         return "twenty minutes to "+text1(h+1)
    #     return "twenty " + text1(m%10) +" to "+text1(h+1)




    return True


h=1
m=1
print("ok:",timeInWords(h,m))