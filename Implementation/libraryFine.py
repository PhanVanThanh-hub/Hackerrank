def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine=0
    if y1==y2:
        if m1==m2:
            if d1>d2:
                fine=15*(d1-d2)
                return fine
            else:
                return fine
        elif m1>m2:
            fine =500*(m1-m2)
            return fine
        else:
            return 0
    elif y1>y2:
        fine=10000*(y1-y2)
    return fine


d1=6
m1=6
y1=2015
d2=9
m2=6
y2=2016
print("ok:",libraryFine(d1, m1, y1, d2, m2, y2))