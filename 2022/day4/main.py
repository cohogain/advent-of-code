f = open('input.txt', 'r')
sequence_1 = []
sequence_2 = []
irange = lambda a, b: range(a, b + 1)

def p1(f):
    counter = 0
    for x in f.read().split("\n"):
        x = x.split(",")

        for _ in range(int(x[0].split("-")[0]), int(x[0].split("-")[1])+1):
            sequence_1.append(_)

        for _ in range(int(x[1].split("-")[0]), int(x[1].split("-")[1])+1):
            sequence_2.append(_)
    
        s1 = set(sequence_1)
        s2 = set(sequence_2)

        if s1.issubset(s2) or s2.issubset(s1):
            counter+=1

        sequence_1.clear()
        sequence_2.clear()

    return counter

def p2(f):
    counter = 0
    for x in f.read().split("\n"):
        x = x.split(",")

        for _ in range(int(x[0].split("-")[0]), int(x[0].split("-")[1])+1):
            sequence_1.append(_)

        for _ in range(int(x[1].split("-")[0]), int(x[1].split("-")[1])+1):
            sequence_2.append(_)
    
        s1 = set(sequence_1)
        s2 = set(sequence_2)

        if s1.intersection(s2) or s2.intersection(s1):
            counter+=1

        sequence_1.clear()
        sequence_2.clear()

    return counter


def p3(f):
    ans = 0
    for l in f:
        a, b = l.strip().split(",")
        a = set(irange(*map(int, a.split("-"))))
        b = set(irange(*map(int, b.split("-"))))
        if len(a & b) > 0:
            ans += 1
    return ans

print(p3(f))