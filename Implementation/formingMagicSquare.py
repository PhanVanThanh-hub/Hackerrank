def formingMagicSquare(s):

    a=[]
    for i in pre:
        total=0
        for j in range(0,3):
            for z in range(0,3):
                total+=abs(i[j][z]-s[j][z])
        a.append(total)
    return min(a)
s=[
    [7, 2, 9],
    [6 ,6 ,2],
    [5 ,1 ,2]
   ]
pre = [#vi  la hinh vuong 3x3 va phai chua cac so 1-9 nen tong cua hinh vuong la 45
        #Dựa theo yêu cầu của bài toán thì chúng ta có thể biết được giá trị của ô giữa [1][1] =5
        #và chúng ta cần tìm 4 cặp số sao cho tổng =10
        #mỗi dòng tổng của nó =15
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],

]
print("ok:",formingMagicSquare(s))