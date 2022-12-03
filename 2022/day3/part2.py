f = open('input.txt', 'r')
lines = f.read().splitlines()
priority_value = 0
priority_sum = 0
elf_group = []

for x, line in enumerate(lines):
    elf_group.append(line)

    if (x+1) % 3 == 0:
        elf_1 = set(elf_group[0])
        elf_2 = set(elf_group[1])
        elf_3 = set(elf_group[2])

        # use intersection() method to get common character
        common_char = list(elf_1 & elf_2 & elf_3)[0]

        # convert character to value
        char_number = ord(common_char)
        if char_number < 97:
            # map UpperCase character values to 27 through 52
            priority_value = (char_number - 38)
        else:
            # map LowerCase character values to 1 through 27
            priority_value = (char_number - 96)

        # add all priority values together
        priority_sum += priority_value

        elf_group.clear()
    
print(priority_sum)