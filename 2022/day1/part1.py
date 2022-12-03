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

            if calorie_sum > most_calories:
                most_calories = calorie_sum

print(most_calories)