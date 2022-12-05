stacks = [['Q','M','G','C','L'], 
['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
['J', 'F', 'D', 'V', 'Q', 'P'],
['N', 'F', 'M', 'S', 'L', 'B', 'T'],
['R', 'N', 'V', 'H', 'C', 'D', 'P'],
['H', 'C', 'T'],
['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
['Z', 'F', 'H', 'G']]

f = open('input.txt', 'r')


def p1(f):
    words = ["move ", "from ", "to "]
    lines = f.read().splitlines()
    for line in lines:
        for word in words:
            line = line.replace(word, "")
        steps = line.split(" ")

        for i in range(0, int(steps[0])):
            stacks[int(steps[2])-1].append(stacks[int(steps[1])-1].pop())
    
    for i in range(0,9):
        print(stacks[i].pop(), end='')

def p2(f):
    words = ["move ", "from ", "to "]
    lines = f.read().splitlines()
    for line in lines:
        for word in words:
            line = line.replace(word, "")
        steps = line.split(" ")
        temp_stack = []

        for i in range(0, int(steps[0])):
            temp_stack.append(stacks[int(steps[1])-1].pop())
            
        temp_stack.reverse()
        for item in temp_stack:
            stacks[int(steps[2])-1].append(item)
        temp_stack.clear()
    
    for i in range(0,9):
        print(stacks[i].pop(), end='')

p2(f)