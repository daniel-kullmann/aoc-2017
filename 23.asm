#set b 79
#set c b
#jnz a 2
#jnz 1 5
#mul b 100
#sub b -100000
#set c b
#sub c -17000
#set f 1
#set d 2
#set e 2
#set g d
#mul g e
#sub g b
#jnz g 2
#set f 0
#sub e -1
#set g e
#sub g b
#jnz g -8
#sub d -1
#set g d
#sub g b
#jnz g -13
#jnz f 2
#sub h -1
#set g b
#sub g c
#jnz g 2
#jnz 1 3
#sub b -17
#jnz 1 -23

def run(a):
    b = 79
    c = b
    if a != 0:
        b *= 100
        b -= 100000
        c = b
        c -= 17000
    while True:
        f = 1
        d = 2
        e = 2
        while True:
            while True:
                g = d
                g *= e
                g -= b
                if g == 0:
                    f = 0
                e -= 1
                g = e
                g -= b
                if g == 0:
                    break
            d -= 1
            g = 1
            g -= b
            if g==0:
                break
        if f == 0:
            h -= 1
        g = b
        g -= c
        if g == 0:
            return h    
        b -= 17

print run(0)
