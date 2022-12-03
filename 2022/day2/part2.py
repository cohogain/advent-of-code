f = open('input.txt', 'r')
lines = f.read().splitlines()
your_score = 0
openent_score = 0
A, X = 1, 1 # rock
B, Y = 2, 2 # paper
C, Z = 3, 3 # scissors

values = {"A": 1, "B": 2, "C": 3}
outcome = {"X": 0, "Y": 3, "Z": 6}
options = {"Rock": 1, "Paper": 2, "Scissors": 3}

for line in lines:
    line = line.split(' ')

    if outcome[line[1]] == 0:
        if values[line[0]] > 1:
            your_choice = values[line[0]]-1
            your_score += values[line[0]]-1
        else:
            your_choice = values[line[0]]+2
            your_score += values[line[0]]+2
        openent_score += 6 + values[line[0]]
    elif outcome[line[1]] == 3:
        your_score += 3 + values[line[0]]
        openent_score += 3 + values[line[0]]
        your_choice = values[line[0]]
    else: 
        if values[line[0]] < 3:
            your_choice = values[line[0]]+1
            your_score += values[line[0]]+1
        else:
            your_choice = values[line[0]]-2
            your_score += values[line[0]]-2
        your_score += 6
    
print(your_score)

