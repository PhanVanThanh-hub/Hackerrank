def quickSort(arr):
    # Write your code here
    equal=arr[0]
    l=[]
    r=[]
    for i in range(1,len(arr)):
        if arr[i]>equal:
            r.append(arr[i])
        else:
            l.append(arr[i])
    l.append(equal)
    a=l+r
    print(a)
    return True

arr=[4, 5, 3, 7, 2]
print("ok:",quickSort(arr))