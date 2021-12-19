def insertionSort2(n, arr):
    i=0
    while i<n-1:
        if arr[i]>arr[i+1]:

            j=i+1
            while j>0:
                if arr[j]<arr[j-1]:
                    x = arr[j-1]
                    arr[j-1] = arr[j]
                    arr[j] = x
                j-=1
        i+=1
        print(' '.join(map(str, arr)))


n=7
arr=[3 ,4 ,7 ,5 ,6 ,2 ,1]
print("ok:",insertionSort2(n,arr))