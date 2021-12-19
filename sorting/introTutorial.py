def introTutorial(V, arr):
    index=-1
    for i in range(0,len(arr)):
        if arr[i]==V:
            index=i
            break

    return index
V=4
arr = [1, 4, 5, 7, 9, 12]
print("ok:",introTutorial(V,arr))
