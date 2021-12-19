def almostSorted(arr):
    a1=arr.copy()
    a1.sort()
    if a1==arr:
        return 0
    a = []
    c=-1
    d=-1
    for i in range(0,len(arr)-1):
        if len(a)!=0:
            break
        if arr[i]>arr[i+1]:
            a.append(arr[i])
            a.append(arr[i+1])
            j=i+1
            for j in range(i+2,len(arr)):
                if arr[j-1]>arr[j]:
                    a.append(arr[j-1])
                else:
                    break
            print("?")
            c=i
            d=j
            print("?",c,':',d,':')
    if arr[d-1]>arr[d]:
        return "no"
    if d+1-c==2:
        return "yes"+"\n"+"swap "+str(c+1)+" "+str(d+1)
    return "yes" + "\n" + "reverse " + str(c+1) + " " + str(d+1)


arr=[3,1,2]
print("ok:",almostSorted(arr))