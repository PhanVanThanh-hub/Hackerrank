import math
def squares(a, b):
    # Write your code here
    a=math.sqrt(a)

    b=math.sqrt(b)
    print(int(a),':',int(b),a,b)
    temp=0
    if a==int(a):
        print("!")
        temp +=1
    for i in range(int(a)+1,int(b)+1):

        temp+=1
    return temp

a=35
b=70
print("ok:",squares(a,b))