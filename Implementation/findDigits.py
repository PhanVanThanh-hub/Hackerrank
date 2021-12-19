def findDigits(n):
    # Write your code here
    temp=0
    a=n
    while n!=0:
        print("?",n)

        if n%10!=0:
            if a%(n%10)==0:
                temp+=1
        n = n // 10

    return temp

n=1203
print("ok:",findDigits(n))