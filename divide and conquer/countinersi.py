arr =[82,12,38,10,15,54,51,71,95,12,1,21,90,10,89,97,42,1,84,92]
# brr=[]
# for i in range(0,len(arr)):
#     brr.append(0)
# def coount(arr,a,b):
#     temp=0
#     if arr[b]>arr[a]:
#         temp += brr[b]
#         for i in range(0,b):
#             if arr[i]>arr[b]:
#                 temp +=1
#         print("r:", temp)
#     else :
#         b=0
#     for i in range(b,a):
#         if arr[i]>arr[a]:
#             print('i:',i,'|a:',a,'|a[i]:',arr[i],'|a[a]:',arr[a])
#             temp +=1
#     brr.insert(a,temp)
#     return temp
# def countInversions(arr):
#     temp = 0
#     b=0
#     for i in range(1,len(arr)):
#         if  arr[i]<arr[i-1]:
#             temp += coount(arr,i,b)
#             b=i
#     return temp
#
# print("ok:",countInversions(arr))
# for i in range(0,len(brr)):
#     print(i,':',brr[i],' ')
temp =0

for i in range(0,len(arr)):
    for a in range(i,len(arr)):
        if arr[i]>arr[a]:
            temp+=1
print("tmep:",temp)