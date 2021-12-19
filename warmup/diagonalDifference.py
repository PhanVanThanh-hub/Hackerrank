def diagonalDifference(arr):
     temp1=0
     temp2=0
     i=0
     j=0
     while i<len(arr) and j<len(arr):
         temp1 +=arr[i][j]
         i+=1
         j+=1

     i = len(arr)-1
     j = 0
     while i >= 0 and j < len(arr):
         print(":",arr[i][j],':',i,':',j)
         temp2 += arr[i][j]
         i -= 1
         j += 1

     return abs(temp2-temp1)
arr=[
[11, 2, 4],
[4, 5, 6],
[10, 8, -12]
]
print("ok:",diagonalDifference(arr))