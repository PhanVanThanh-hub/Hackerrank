import re
def minimumNumber(n, password):
    temp =0
    if not re.search("[a-z]", password):
        temp +=1
    if not re.search("[A-Z]", password):
        temp +=1
    if not re.search("[0-9]", password):
        temp +=1
    if not re.search("[!@#$%^&*()+]", password):
        temp +=1
    if  re.search("-", password) and not re.search("[!@#$%^&*()+]", password) :
        temp -=1
    if n<6:
        a= 6-n
        if temp==0:
            temp += a
        else:
            if a>temp:
                temp =a
    return temp

n=7
password="AUzs-nV"
print(minimumNumber(n,password))