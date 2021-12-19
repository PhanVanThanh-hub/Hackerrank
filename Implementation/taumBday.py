def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc<wc:
        if bc+z<wc:
            return bc*b+(bc+z)*w
    elif bc>wc:
        if wc+z<bc:
            return wc*w+(wc+z)*b

    return b*bc+w*wc

b = 3
w = 3
bc = 1
wc = 9
z = 2

print("ok:",taumBday(b,w,bc,wc,z))
