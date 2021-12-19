def bigSorting(unsorted):

    a = []
    x = len(unsorted)
    for i in range(0,len(unsorted)):
        unsorted[i]=int(unsorted[i])
    while x > 0:
        c = min(unsorted)

        a.append(c)
        unsorted.remove(c)
        x = len(unsorted)
        print(c, ':', unsorted)

    return a

unsorted=["31415926535897932384626433832795",

"1",
"3",
"10",
"3",
"5"]
print("ok:",bigSorting(unsorted))