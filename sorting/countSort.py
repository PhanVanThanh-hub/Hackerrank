def countSort(arr):
    # Write your code here



    for i in arr:
        i[0]=int(i[0])
    for i in range(0,len(arr)//2):
        arr[i][1]="-"
    arr.sort(key=lambda tup: tup[0])
    print(arr)
    for i in arr:
        print(i[1],end="")
    # a=[]
    # i=0
    # x=len(arr)
    # while x!=i:
    #     for j in arr:
    #         if j[0]==i:
    #             a.append(j)
    #     i+=1
    #     x=len(arr)
    # a1=arr[0:len(arr)//2]
    # print(a1)
    # print(a)
    # c=[]
    # for i in a:
    #     if i in a1:
    #         c.append("-")
    #         a1.remove(i)
    #     else:
    #
    #         c.append(i[1])
    #
    # print(' '.join(map(str,c)))



    return True
arr=[
[1 ,'e'],
[2 ,'a'],
[1 ,'b'],
[3 ,'a'],
[4 ,'f'],
[1 ,'f'],
[2 ,'a'],
[1 ,'e'],
[1 ,'b'],
[1 ,'c'],
]
# arr=[
# [0 ,'ab'],
# [6,'cd'],
# [0 ,'ef'],
# [6 ,'gh'],
# [4 ,'ij'],
# [0 ,'ab'],
# [6 ,'cd'],
# [0 ,'ef'],
# [6 ,'gh'],
# [0 ,'ij'],
# [4 ,'that'],
# [3 ,'be'],
# [0 ,'to'],
# [1 ,'be'],
# [5 ,'question'],
# [1 ,'or'],
# [2 ,'not'],
# [4, 'is'],
# [2 ,'to'],
# [4 ,'the']
# ]
print("ok:",countSort(arr))