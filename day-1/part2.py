import collections

def part2():
    res = 0
    two_occurence = collections.defaultdict(int)
    one_arr = []
    with open('part1input.txt', 'r') as file:
        for line in file:
            one,two = line.split()
            one_arr.append(int(one))
            two_occurence[int(two)] += 1
    for one in one_arr:
        res += one * two_occurence[one]
    return res

if __name__ == '__main__':
    print(part2())