#https://www.hackerrank.com/challenges/jim-and-the-orders/problem
def jimOrders(orders):
    arr=[]
    for i in orders:
        arr.append(i[0]+i[1])
    print("huh:",arr)
    reslut=[arr[0]]
    reslut1=[1]
    for i in range(1,len(arr)):
        hehe=-1
        reslut.sort()
        print("---------",reslut)

        for j in range(len(reslut)):
            if arr[i]<reslut[j]:
                print("?",arr[i],':',reslut[j])
                reslut.append(arr[i])
                if j==0:
                    reslut1.insert(0, i + 1)
                else:
                    reslut1.insert(j,i+1)

                hehe=1
                break
        if hehe==-1:
            print(reslut1)
            print("as:",arr[i])
            reslut1.insert(j+1, i + 1)
            print(reslut1)
            reslut.append(arr[i])
        print("???:",reslut1)
    print("??",reslut1)
    print("d",reslut)
    return reslut1

# order=[[8 ,1],[4, 2],[5, 6],[3, 1],[4, 3]]
order =[[1,1],[1,1]]
print("hsa:",jimOrders(order))