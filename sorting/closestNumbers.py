def closestNumbers(arr):
    # Write your code here
    arr.sort()
    a=[]
    max=abs(arr[0]-arr[1])
    a.append(arr[0])
    a.append(arr[1])
    for i in range(1,len(arr)-1):
        b=[]
        si=abs(arr[i]-arr[i+1])
        if len(a)!=0:
            if si==max:
                a.append(arr[i])
                a.append(arr[i+1])
            elif si<max:
                max=abs(arr[i]-arr[i+1])
                a.clear()
                a.append(arr[i])
                a.append(arr[i + 1])

    return a

arr=[-20 ,-3916237 ,-357920 ,-3620601 ,7374819, -7330761 ,30 ,6246457 ,-6461594 ,266854 ,-520 ,-470 ]
print("ok:",closestNumbers(arr))