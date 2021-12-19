def countA(s):
    temp = 0
    for i in range(0,len(s)//2):
        if s[i]!=s[-i-1]:
            temp+=1
    return temp
def highestValuePalindrome(s, n, k):
    # Write your code here
    a=countA(s) #Tinh so cap chua doi xung
    for i in range(0,len(s)):
        if s[i]==s[-i-1]:
            if s[i]=="9":#kiem tra xem cap so doi xung do co phai la gtri max chua
                continue
            elif k-2>=a:#kiem tra xem so cap chua doi xung va so lan duoc xoay.
                        # Neu nhu so lan xoay +2>= so cap chua doi xung thi chuyen
                        #cap doi xung thanh 9 9 de ra so lon nhat
                s = s[:i] + "9" + s[i + 1:]
                s = s[:len(s) - i - 1] + "9" + s[len(s) - i:len(s) + 1]
                k-=2    #vi thay the 2 so nen so lan xoay -2
        elif s[i]!=s[-i-1]:#neu nhu chua doi xung
            if s[i]=="9":
                # k-1>=a-1:Ktra xem co the xoay them nua ko
                if k-1>=a-1:
                    s = s[:len(s) - i - 1] + "9" + s[len(s) - i:len(s) + 1]
                    k-=1
                    a-=1
                else:
                    return -1
            elif s[-i-1]=="9":
                if k-1>=a-1:
                    s = s[:i] + "9" + s[i + 1:]
                    k-=1
                    a-=1
                else:
                    return  -1
            else:
                if k-2>=a-1:#Kiem tra xem co the xoay 2 lan hay ko tai dem i va -i hay ko
                            # De chuyen 2 gtri do ve ="9"
                    s = s[:i] + "9" + s[i + 1:]
                    s = s[:len(s) - i - 1] + "9" + s[len(s) - i:len(s) + 1]
                    k-=2
                    a-=1
                elif k-1>=a-1:
                    if s[i]<s[-i-1]:
                        s = s[:i] + s[-i - 1] + s[i + 1:]
                    elif s[i]>s[i-1]:
                        s = s[:len(s) - i - 1] + s[i] + s[len(s) - i:len(s) + 1]
                    a-=1
                    k-=1
                else:
                    return -1

    if s%2!=0:#kiem tra xem chieu dai la chan hay le.Neu chan thi bo qua
        if k>0:#kiem tra xem con so lan quay hay khong
                #Neu con thi chen "9" vao giua de tro thanh chuoi lon nhat
            s = s[:len(s) // 2] + "9" + s[len(s) // 2 + 1:]
    return s

n = 4
k =1
s = '0011'

print("ok:",highestValuePalindrome(s,n,k))