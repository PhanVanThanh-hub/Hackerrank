def howManyGames(p, d, m, s):
    if s < p:
        return 0
    temp = 0
    while s >= 0:
        if p > s:
            break
        s -= p
        temp += 1
        if p - d <= m:
            p = m
            break
        else:
            p -= d

    temp += (s // p)
    return temp
p=100
d=1
m=1
s=99
print("ok:",howManyGames(p,d,m,s))