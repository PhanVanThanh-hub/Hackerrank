import re
def findNumberFist(s):
     b = -1
     a = len(s) // 2
     i = 1
     c = int(s[0])
     x = len(str(s))
     if int(s[a:x]) - int(s[0:a]) == 1:
          b = int(s[0:a])
          return b
     x1=len(s)//3
     if x1!=0:
          if int(s[x1:x-x1])-int(s[0:x1])==1:
               b=int(s[0:x1])
               return b
     while i < len(s):
          x = len(str(c))
          if b == -1:
               if int(s[i:i + x]) - c == 1:
                    b = c
                    if len(str(b))==1:
                         d = b * 10 + int(s[i])
                         z = len(str(b))
                         if int(s[i+1:i+2+z]) - d == 1:
                              b=d
               if b == -1:
                    if int(s[i:i+x])-c<0:
                         if int(s[i:i+1+x])-c==1:

                              b=c
                    if int(s[i]) - c != 1:
                         c = c * 10 + int(s[i])
                    else:
                         b = c
               if x == a:
                    break
          else:
               return b
          i += 1
     return b
s="13"

def separateNumbers(s):
     if len(s)<=1 or s[0]=="0":
          print("NO")
     else:
          print("fist:",findNumberFist(s))
          a=findNumberFist(s)
          x=len(str(a))
          c=1
          q=0
          i=x

          if int(s[0:i][-1])==9:
               if not re.search("[0-8]", (s[0:i])):
                    x += 1
          while i< len(s):
               print("lmai:", (s[i:i + x]))
               if int(s[i:i+ x]) - a != c:
                    print("NO")
                    q=-1
                    break
               c+=1
               if not re.search("[0-8]",(s[i:i+ x])):
                    x += 1
                    i -=1
               i += x

          if q!=-1 :
               if a == -1:
                    print("NO")
               else:
                    print("YES "+str(a))

separateNumbers(s)