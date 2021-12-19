st=0
for i in range(1,134):
        if i>=10 and i<100:
            st = st*10+i//10
            st = st * 10 + (i % 10)
        elif i>=100:
            st = st * 10 + i // 100
            st = st * 10 + (i // 10)%10
            st = st * 10 + (i % 10)
        else:
            st=st*10+i
        print("sT:",st)
print(st)