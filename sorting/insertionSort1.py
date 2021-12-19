def insertionSort1(n, arr):
    x=arr[-1]
    i=n-2
    while arr[i]>x and i>=0:
        arr[i+1]=arr[i]
        print(arr)
        i-=1
    arr[i+1]=x
    print(arr,x,i+1)

n=5
arr=[2 ,4 ,6 ,8 ,3]
print("ok:",insertionSort1(n,arr))