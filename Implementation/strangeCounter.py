def strangeCounter(t):
    # Write your code here
    i=3
    b=3
    while b<t:
        i=i*2
        b+=i
    return b-t+1
t=10
print("ok:",strangeCounter(t))