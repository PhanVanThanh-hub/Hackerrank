def repeatedString(s, n):
    temp = 0
    for i in s:     #Đếm số lượng kí tự a có trong chuỗi
        if i == "a":
            temp += 1
    if temp == 0:
        return 0
    print("temp:",temp)
    l = n / len(s)#Tính số lần lặp lại nguyên chuỗi s
    if l == int(l):#Nếu như lặp lại cả chuỗi mà không ...
        temp *= l
    else:
        temp *= (n // len(s))
        l = n % len(s)
        for i in range(0, l + 1):
            if s[i] == "a":
                temp += 1
    return int(temp)


s = "jdiacikk"
n = 899491

print("ok:", repeatedString(s, n))
