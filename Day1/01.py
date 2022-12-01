if __name__ == '__main__':
    max_score = [0]
    with open('input.txt', 'r') as f:
        calories = 0
        for line in f.read().splitlines():
            if len(line) != 0:
                calories += int(line)
            else:
                max_score.append(calories)
                calories = 0
    max_score.sort()
    total_calories = 0
    for score in max_score[-3:]:
        total_calories += score
    print(total_calories)