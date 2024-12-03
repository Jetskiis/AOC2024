
def part1():
    group_1 = []
    group_2 = []
    with open('part1input.txt', 'r') as file:
        for line in file:
            one,two = line.split()
            group_1.append(one)
            group_2.append(two)
    res = 0
    group_1.sort()
    group_2.sort()
    for i in range(len(group_1)):
        res += abs(int(group_1[i]) - int(group_2[i]))
    return res

if __name__ == '__main__':
    print(part1())

