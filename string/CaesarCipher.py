import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# k=87
# s="www.abc.xy"
k=45
s="DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy."
def caesarCipher1(s, k):
    a=""
    if k>25:
        k=k%26
    for i in range(0,len(s)):
        if (ord(s[i])>=97 and ord(s[i])<=122):
            c=ord(s[i])+k
            if c>122:
                a +=chr(96+c-122)
            else:
                a +=chr(c)
        elif (ord(s[i])>=65 and ord(s[i])<=90):
            c=ord(s[i])+k
            if c>90:
                a +=chr(64+c-90)
            else:

                a +=chr(c)
        else:
            a += chr(ord(s[i]))
    return a
print("ok:",caesarCipher1(s,k))