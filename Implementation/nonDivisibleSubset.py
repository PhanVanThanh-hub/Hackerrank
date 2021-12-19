def nonDivisibleSubset(k, s):
    # Write your code here
    a=[]
    # for i in range(0,len(s)-1):
    #     b=[]
    #     b.append(s[i])
    #     # if len(s) - i < len(a):
    #     #     break
    #
    #     for j in range(i+1,len(s)):
    #         # if len(b)+len(s)-j<len(a):
    #         #     break
    #         if (s[i]+s[j])%k!=0  :
    #             if len(b)!=0:
    #                 temp=0
    #                 for z in range(0,len(b)):
    #                     if (b[z]+s[j])%k==0:
    #                         temp=1
    #                         break
    #                 if temp==0:
    #                     b.append(s[j])
    #     print("?:",len(b),':',b)
    #     if len(b)>len(a):
    #         a=b
    # i=0
    # x=len(s)
    # while x>0:
    #     b=[]
    #     b.append(s[i])
    #     print("s:",x)
    #     d=[]
    #     d.append(s[i])
    #     for z in range(0, len(a)):
    #         if (s[i] + a[z]) % k != 0:
    #             b.append(a[z])
    #     for j in range(i+1,x):
    #         if (s[i]+s[j])%k!=0:
    #             temp=0
    #             for z in range(0,len(b)):
    #                 if (s[j]+b[z])%k==0:
    #                     temp=1
    #                     break
    #             if temp==0:
    #                 b.append(s[j])
    #                 d.append(s[j])
    #     if len(b)>len(a):
    #         a=b
    #     for z in d:
    #         while z in s:
    #             s.remove(z)
    #
    #     print("b:",b)
    #     print("a:",a)
    #     print("?:",s)
    #     print("d:",d)
    #     print("______________")
    #     x=len(s)
    #
    # print("a:",a)
    #(A+B)%K==0 <=> A%K+B%K==K =>phần dư của 2 gtri A và B sẽ có dạng i và k-i
    counts = [0] * k # tạo mảng counts gồm k phần tử
    print("co:",counts)
    for number in s:
        counts[number % k] += 1 #Đếm số lượng của mỗi phần dư trong mảng

    count = min(counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(counts[i], counts[k - i])#Lấy số lượng phần dư lớn hơn theo từng cặp
    if k % 2 == 0:                                #Vì phần dư i+ k-i sẽ ==k nên chỉ có 1 phần dư được chọn
        count += 1                                #Bouns:chỉ phần dư i + k-i ==k
    return count
n = 4
k = 5
s= [770528134, 663501748 ,384261537 ,800309024 ,103668401 ,538539662 ,385488901 ,101262949 ,557792122 ,46058493]
print("ok:",nonDivisibleSubset(k,s))