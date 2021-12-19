def pageCount(n, p):
    temp = 0
    temp1 = -1

    if (p + 1 == n and n%2!=0) or p == n or p==1:
        return 0
    if n-p==1:
        return 1
    i = 1
    while i <p:
        temp += 1
        i += 2
    j = n
    while j >= p:
        temp1 += 1
        j -= 2
    print(temp,':',temp1)
    return min(temp1, temp)
n=5
p=4
print("pk:",pageCount(n,p))