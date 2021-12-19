def beautifulTriplets(d, arr):
    temp=0
    x=len(arr)
    for i in range(0,x-2):
        for j in range(i+1,x-1):
            if arr[j]-arr[i]==d:
                for k in range(j+1,x):
                    if arr[k]-arr[j]==d:
                        temp+=1
                        break

    return temp
d=3
arr = [1, 2, 4, 5, 7, 8, 10]
print("ok:",beautifulTriplets(d,arr))