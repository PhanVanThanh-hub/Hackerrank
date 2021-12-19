def queensAttack(n, k, r_q, c_q, obstacles):
    # for z in range(0,k):
    #     print("a:",obstacles[z][0])
    #     for i in range(n,0 ,-1):
    #         print("",i)
    #         for j in range(1,n+1):
    #             if i == r_q and j == c_q:
    #                 print("?",end=" ")
    #             else:
    #                 print("i", end=" ",)
    temp=0
    obstacles = {(ob[0], ob[1]) for ob in obstacles}#Chuyển list thành set
    c1 = r_q
    c2 = c_q
    print("tmep:", temp)
    while c2 > 0:
        d = []
        c2 -= 1
        d.append(c1)
        d.append(c2)
        print("d:", d)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("--------------")
    c1 = r_q
    c2 = c_q
    print("tmep:", temp)
    while c2 < n:
        d = []
        c2 += 1
        d.append(c1)
        d.append(c2)
        print("d:", d)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("--------------")
    c1 = r_q
    c2 = c_q
    print("tmep:", temp)
    while c1 < n:
        d = []
        c1 += 1
        d.append(c1)
        d.append(c2)
        print("d:", d)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("--------------")
    c1 = r_q
    c2 = c_q
    print("tmep:", temp)
    while c1 > 0:

        d = []
        c1 -= 1
        d.append(c1)
        d.append(c2)
        print("d:", d)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("--------------")
    c1=r_q
    c2=c_q
    print("tmep:",temp)
    while c2>0 and c1<n:
        d=[]
        c1+=1
        c2-=1
        d.append(c1)
        d.append(c2)
        print("d:",d)
        if d not in obstacles:
            print("c:",c1,':',c2)
            temp+=1
        else:
            break
    print("--------------")
    c1 = r_q
    c2 = c_q
    while c2<n:
        d = []
        c1-=1
        c2+=1
        d.append(c1)
        d.append(c2)
        print("d:", d)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("--------------")
    c1 = r_q
    c2 = c_q
    while c2 >1 and c1>1:
        d = []
        c1 -= 1
        c2 -= 1
        d.append(c1)
        d.append(c2)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("temp:",temp)
    print("--------------")
    c1 = r_q
    c2 = c_q
    while c1 <n:
        d = []
        c1 += 1
        c2 += 1
        d.append(c1)
        d.append(c2)
        if d not in obstacles:
            print("c:", c1, ':', c2)
            temp += 1
        else:
            break
    print("temp:", temp)


    return temp

n=5
k=3
r_q=4
c_q=3
obstacles=[[4 ,2],  [5,5],[2,3] ]
print("ok:",queensAttack(n, k, r_q, c_q, obstacles))