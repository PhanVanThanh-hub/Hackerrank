def minimumDistances(a):
    # Write your code here
    min=-1
    for i in range(0,len(a)-1):
        cou=0
        for j in range(i+1,len(a)):
            cou+=1
            if cou >min and min !=-1:
                break
            if a[i]==a[j]:
                print("1:",min)
                min=j-i
                break
    print("min:",min)
    return min

a= [7, 1, 3, 4, 1, 7]
print("ok:",minimumDistances(a))