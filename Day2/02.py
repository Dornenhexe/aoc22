# A/X - Rock - 1 Point
# B/Y - Paper - 2 Points
# C/Z - Scissor - 3 Points
# Loss - 0 Points, Draw - 3 Points, Win - 6 Points
if __name__ == '__main__':
    max_score = 0
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            elf = line[0]
            self = line[2]
            if self == 'X':     # Rock
                max_score += 1
                if elf == 'A':  # Draw
                    max_score += 3
                elif elf == 'C':    # Win
                    max_score += 6
            elif self == 'Y':   # Paper
                max_score += 2
                if elf == 'A':  # Win
                    max_score += 6
                elif elf == 'B':    # Draw
                    max_score += 3
            elif self == 'Z':   # Scissor
                max_score += 3
                if elf == 'B':  # Win
                    max_score += 6
                elif elf == 'C':    # Draw
                    max_score += 3
    print(max_score)

# A - Rock - 1 Point
# B - Paper - 2 Points
# C - Scissor - 3 Points
# X - Loss - 0 Points
# Y - Draw - 3 Points
# Z - Win - 6 Points
    max_score = 0
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            elf = line[0]
            self = line[2]
            if self == 'X':  # Loss
                if elf == 'A':  # Rock
                    max_score += 3
                elif elf == 'B':  # Paper
                    max_score += 1
                elif elf == 'C':  # Scissor
                    max_score += 2
            if self == 'Y':  # Draw
                max_score += 3
                if elf == 'A':  # Rock
                    max_score += 1
                elif elf == 'B':  # Paper
                    max_score += 2
                elif elf == 'C':  # Scissor
                    max_score += 3
            if self == 'Z':  # Win
                max_score += 6
                if elf == 'A':  # Rock
                    max_score += 2
                elif elf == 'B':  # Paper
                    max_score += 3
                elif elf == 'C':  # Scissor
                    max_score += 1
    print(max_score)