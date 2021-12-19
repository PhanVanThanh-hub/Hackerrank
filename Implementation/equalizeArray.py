def equalizeArray(arr):
    a= list(set(arr))
    max=0
    c=-1
    for i in a:
        x=arr.count(i)
        print("x:",x,':',i)
        if x>max:
            max=x
            c=i
    print(c,':',max)
    return len(arr)-max
arr=[3,2,3,3,1,1]
print("ok:",equalizeArray(arr))