f = open('input.txt', 'r').read()

def p1(f):
    position = 0
    for x in range(0, int(len(f))):
        check_start = [f[y] for y in range(x, x+4)]
        if len(check_start) == len(set(check_start)):
            position = x + 4
            break
        check_start.clear()
    print(position)

def p2(f):
    position = 0
    for x in range(0, int(len(f))):
        check_start = [f[y] for y in range(x, x+14)]
        if len(check_start) == len(set(check_start)):
            position = x + 14
            break
        check_start.clear()
    print(position)

p2(f)