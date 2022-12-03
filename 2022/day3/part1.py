f = open('input.txt', 'r')
lines = f.read().splitlines()
priority_value = 0
priority_sum = 0

for line in lines:
    # length of line
    length = len(line)

    # middle of line
    middle = length // 2

    # first half of line
    first_sack = line[:middle]

    # second half of line
    second_sack = line[middle:]

    # convert strings into sets
    first_sack_set = set(first_sack)
    second_sack_set = set(second_sack)

    # use intersection() method to get common character
    common_char = list(first_sack_set.intersection(second_sack_set))[0]

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
    
print(priority_sum)
