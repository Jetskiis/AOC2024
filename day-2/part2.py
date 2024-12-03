def part1(level):
    res = 0
    for i in range(1,len(level)):
        if i >= 2:
            if (int(level[i - 1]) < int(level[i]) and int(level[i - 2]) > int(level[i - 1])) or (int(level[i - 1]) > int(level[i]) and int(level[
                                                                                                                                               i - 2]) < int(level[i - 1])):
                break
        if not(abs(int(level[i-1]) - int(level[i])) >= 1 and abs(int(level[i-1]) - int(level[i])) <= 3):
            break
        if i == len(level) - 1:
            res += 1
    return res

def part2():
    res = 0
    with open('part1input.txt', 'r') as file:
        for line in file:
            level = line.split()
            for i in range(len(level)):
                input = level[:i] + level[i+1:]
                if part1(input):
                    res += 1
                    break

    return res


if __name__ == '__main__':
    print(part2())
