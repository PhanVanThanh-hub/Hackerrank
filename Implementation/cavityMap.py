def cavityMap(grid):
    # Write your code here
    a=[]
    for i in grid:
        b=[]
        x=len(grid)
        z=0
        while z!=x:
            b.append(i[z])
            z+=1
        a.append(b)
    print(a)
    temp=0
    for i in range(1,len(a)-1):

        print("------")
        for j in range(1,len(a)-1):
            print(a[i][j])
            if a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1] and a[i][j]>a[i+1][j] and a[i][j]>a[i-1][j]:
                a[i][j]="x"
        print("------")
    print(a)
    c=[]
    for i in a:
        b=""
        for j in i:
            b+=str(j)
        c.append(b)
    return c

grid = ['1112', '1912', '1892', '1234']
print("ok:",cavityMap(grid))