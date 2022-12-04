if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        priority = 0 # sum of items which occur in both compartments
        for line in f.read().splitlines():
            compartment1 = set(line[0:int(len(line)/2)])
            compartment2 = set(line[int(len(line)/2):len(line)])
            item = compartment1.intersection(compartment2)
            for char in item:
                temp = ord(char) # in ascii
                if temp > 90: # lower case
                    temp -= 96
                else:
                    temp -= 38 # upper case
            priority += temp
    print(priority)

# Part 2
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        elf_counter = 0
        rucksacks = []
        priority_type = 0
        for line in f.read().splitlines():
            rucksacks.append(set(line))
            elf_counter += 1
            if elf_counter % 3 == 0: # always compare 3 elf-rucksacks
                badge1 = rucksacks[-3].intersection(rucksacks[-2])
                badge = badge1.intersection(rucksacks[-1])
                for char in badge:
                    temp = ord(char)  # in ascii
                    if temp > 90:  # lower case
                        temp -= 96
                    else:
                        temp -= 38  # upper case
                    priority_type += temp
    print(priority_type)