def gemstones(arr):
    a=[]
    x=min(arr, key=len) #lấy chuỗi có độ dài ngắn nhaasst trong mảng
    arr.remove(x) #xóa chuỗi có độ ngắn nhỏ nhất trong mảng
    x=list(set(x)) # xóa các kí tự trùng nhau trong chuỗi
    for i in x:
        temp =0
        b=[]
        for j in arr: #lấy từng chuỗi trong mảng
            for z in j: #lấy từng kí tự trong chuỗi so sánh với mỗi kí tự của mảng x
                if z==i:
                    temp+=1
            if temp ==0:#nếu kí tự i trong x có xuất hiện trong 1 chuỗi của arr thì chèn 1 và ngược lại
                b.append(0)
                break
            else:
                b.append(1)
            temp=0
        if 0 not in b:# kiểm tra xem kí tự i trong mảng x không xuất hiện trong chuỗi nào hay ko,nếu có thì chèn 1 còn ko thì bỏ qua
            a.append(1)
    return len(a)

arr=['abcdde' ,'baccd', 'eeabg']
print("ok:",gemstones(arr))