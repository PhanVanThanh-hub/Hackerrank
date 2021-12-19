def queensAttack(n, k, r_q, c_q, obstacles):
    print("?:", type(obstacles))
    obstacles = {(ob[0],ob[1]) for ob in obstacles}
    print("?:",type(obstacles))
    mvs, count = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)], 0

    for m in mvs:
        cr, cc = r_q, c_q
        while (cr + m[0] >= 1 and cr + m[0] <= n) and (cc + m[1] >= 1 and cc + m[1] <= n):
            cr += m[0]
            cc += m[1]
            if (cr, cc) in obstacles:break
            count += 1

    return count
n=5
k=3
r_q=4
c_q=3
obstacles=[[4 ,2],  [5,5],[2,3] ]
print("ok:",queensAttack(n, k, r_q, c_q, obstacles))
