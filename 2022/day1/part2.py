f = open('input.txt', 'r')
lines = f.read().splitlines()
elf_calorie_list = []
elf_stock = []
most_calories = 0
elf_counter = 0
elf_id = 0
N = 3

for line in lines:
    if line != '' and line != lines[:-1]:
        elf_calorie_list.append(int(line))
    else:
        elf_counter += 1
        if elf_calorie_list:
            calorie_sum = sum(elf_calorie_list)
            elf_stock.append((elf_counter, int(calorie_sum)))
            elf_calorie_list.clear()

elf_stock.sort(key=lambda tup: tup[1])

top_N = elf_stock[-N:]
most_calories= sum([int(top[1]) for top in top_N])

print(most_calories)