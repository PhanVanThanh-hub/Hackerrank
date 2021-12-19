def circularArrayRotation(a, k, queries):
    d=a.copy()
    #Thuật toán basic
    if k%len(a)!=0:
        for i in range(0,k%len(a)):
            b=a.copy()
            for j in range(1,len(a)):
                a[j]=b[j-1]#phần tử sau = phần tử trước
                if j==len(a)-1:
                    a[0]=b[-1]#phần tử đầu = phần tử cuối

    c=[]
    print(a)
    for i in queries:
        c.append(a[i])
    print("c:",c)
    c=[]
    #Thuat toán xoay mảng tối ưu nhất
    for i in range(0, k%len(a)):
        p = d.pop(-1)#xóa gtri cuối của mảng
        d.insert(0, p)#chèn gtri vừa xóa vào đầu mảng
    for i in queries:
        c.append(a[i])
    print("c2:", c)
    return c


    return True
a=[3,4,5,12,2,9,11]
k=9
queries=[1,3]
print("ok:",circularArrayRotation(a,k,queries))