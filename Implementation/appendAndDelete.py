#https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def appendAndDelete(s, t, k):
    s1=len(s)
    t1=len(t)
    if (s1==t1 and k==s1*2+1) or(s1==t1 and k==s1*2):
        if k==s1*2+1 or k==s1*2:
            return "YES"        #xet truong hop chieu dai 2 mang = nhau:
                                #Nếu như số lần thực hiện gấp đôi or (gấp đôi +1)
                                #chiều dải của chuổi thì trả về yes
    s2=s
    if s1-t1>=1:          #Đưa chiều dài chuỗi 1 về = chiều dài chuỗi 2
        s=s[:s1-(s1-t1)]
    index=-1
    for i in range(len(s)-1,-1,-1):#Lấy vị trí kí tự chuỗi 1 xa nhất khác chuỗi 2
        if s[i]!=t[i]:             #Vị chỉ xóa được kí tự cuối nên ưu tiên lặp từ cuối lên trên
           index=i                 #Có thể lặp từ 0->len(s) và dừng lại khi gặp 2 kí tự khác nhau
    if index !=-1:
        s=s[:index]
        if index==0:            #Kiểm tra xem vị trí xóa có phải =0
            k-=len(s2)          #Hoặc có thể ktra len(s)==0
            if k>=len(t):       #Nếu như ==0 thì kiểm tra xem số lần thực hiện sau khí xóa hết chuỗi
                return "Yes"    #Có còn lớn hơn hoặc = chiều dài chuỗi 2.Nếu lớn hơn thì Yes
            return "No"
    k=k-(len(s2)-len(s))
    if len(s)<len(t) and len(t)-len(s)>1 :#chuỗi sau khi thực hiện xóa
        if k%(len(t)-len(s))==0 :
            return "Yes"
        return "No"
    # if len(s)==t1 and k==len(s)*2+1:
    #     return "Yes"
    if k==len(t)-len(s) or (len(t)==len(s) and (k%2==0 or k>=len(s)*2+1 )):
        return "YES"  #Nếu như len chuỗi 2 - chuỗi 1 ==k thì  chuỗi 1có thể thực kiện chèn k lần để = chuỗi 2
    else:             #Nếu như len 2  chuỗi = nhau thì ktra số lên còn lại của k
                      #Nếu k%2==0:có thể thực hiện k/2 số lần xóa và chèn
                      #Nếu k>=len(s)*2+1: đưa mảng về chuỗi rỗng >=1 lần và thực hiện len(s2) lần chèn
        return "NO"
    return True

s="zzzzz"
t="zzzzzzz"
k=4
print("ok:",appendAndDelete(s,t,k))