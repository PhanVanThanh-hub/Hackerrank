def findMedium(a,d):

    count=0
    m1=None
    print(":",a)
    for val,index in enumerate(a):
        count +=index
        print(count,end=" ")
        if m1==None and count>=d//2:
            m1=val
        if count>=d//2+1:
            m2=val
            break
    medium=m2
    print('?',medium)
    if d%2==0:
        medium=0.5*(m1+m2)
    return medium
def activityNotifications(expenditure, d):
    # temp=0
    # a=[]
    # for i in range(0,d):
    #     a.append(expenditure[i])
    # print(a)
    # for i in range(0,len(expenditure)-d):
    #     medium=0
    #     medium=sum(a)/d
    #     print(i, ':', i + d,':',expenditure[i+d],':',medium)
    #     if expenditure[i+d]>=medium*2:
    #         temp+=1
    #     a.pop(0)
    #     a.append(expenditure[i])
    # print(temp)
    # return True

    a=[0]*201                   #Sử dụng phương pháp chèn đếm
    for i in expenditure[0:d]:
        a[i]+=1
    print(a)
    count=0
    for i in range(d,len(expenditure)):
        if expenditure[i]>=findMedium(a,d)*2:
            count+=1
            a[expenditure[i-d]]-=1
            a[expenditure[i+1]]+=1
    print(count)

ex=[2, 3, 4 ,2, 3, 6 ,8 ,4 ,5]
d=5
print("ok:",activityNotifications(ex,d))