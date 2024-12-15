def part1(times):
    input = [[int(token) for token in line.split(" ")] for line in open('input.txt').read().split("\n")]

    cur = input[0]
    for i in range(times):
        newCur = []
        for val in cur:
            if val == 0:
                newCur.append(1)
            elif len(str(val)) % 2 == 0:
                val1, val2 = int(str(val)[:len(str(val)) // 2]), int(str(val)[len(str(val)) // 2:])
                newCur.extend([val1,val2])
            else:
                newCur.append(val * 2024)
        cur = newCur
    return len(cur)


if __name__ == '__main__':
    print(part1(25))

