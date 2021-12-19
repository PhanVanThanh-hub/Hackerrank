def migratoryBirds(arr):
    # Write your code here

    i = 0
    max = 0
    ch = 0
    d=list(set(arr))
    print(d)
    x = len(d)
    while i < x:
        c = arr.count(d[i])

        if c > max:
            max = c
            b = arr[i]
            ch = ch - ch + d[i]

        i += 1
    return ch
arr=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
print("ok:",migratoryBirds(arr))