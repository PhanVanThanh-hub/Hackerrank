def viralAdvertising(n):
    share=5
    cumulative=2
    like=2
    if n==1:
        return cumulative
    for i in range(2,n+1):
        share=like*3
        like = share//2
        cumulative +=like
        if i==n:
            return cumulative
    return 0

n=5
print("ok:",viralAdvertising(n))
