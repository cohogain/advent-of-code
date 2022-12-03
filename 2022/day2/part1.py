f = open('input.txt', 'r')
lines = f.read().splitlines()
your_score = 0
openent_score = 0
A, X = 1, 1 # rock
B, Y = 2, 2 # paper
C, Z = 3, 3 # scissors

values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
options = {"Rock": 1, "Paper": 2, "Scissors": 3}

for line in lines:
    line = line.split(' ')
    max_num = max(values[line[0]], values[line[1]])
    min_num = min(values[line[0]], values[line[1]])
    openent_score += values[line[0]]
    your_score += values[line[1]]
    if abs(values[line[0]]-values[line[1]]) == 1:
        if values[line[0]] < values[line[1]]:
            your_score += 6
        else:
            openent_score += 6
    elif abs(values[line[0]]-values[line[1]]) == 2:
        if values[line[0]] > values[line[1]]:
            your_score += 6
        else: 
            openent_score += 6
    else:
        your_score += 3
        openent_score += 3

print(your_score)

