def run(a):
    h = 0
    number = 79
    end = number
    if a != 0:
        number *= 100
        number += 100000
        end = number + 17000
        print number, end
    while number != end:
        flag = 1
        d = 2
        e = 2
        while d != number:
            while e != number:
                if d*e == number:
                    flag = 0
                e += 1
            d += 1
        if flag == 0:
            h += 1
        number += 17
    return h    

print run(1)
