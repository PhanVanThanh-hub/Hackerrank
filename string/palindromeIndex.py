
def palindromeIndex(s):
    # Write your code here
    index=len(s)-1
    for i in range(len(s)//2):
        if s[i]!=s[index]:
            if s[i + 1] != s[index] or s[i+2]!= s[index-1] :
                return index
            return i
        index-=1
    return -1
str="hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"

print("s:",palindromeIndex(str))