def part1():
    res = []
    cnt = 0
    for idx,char in enumerate(open('input.txt').read()):
        if idx % 2 == 0:
            res.extend([str(cnt) for i in range(int(char))])
            cnt+=1
        else:
            res.extend(['.' for i in range(int(char))])

    l, r = 0, len(res) - 1
    while l < r:
        while l < r and res[l] != '.':
            l += 1
        while l < r and res[r] == '.':
            r -= 1
        res[l], res[r] = res[r], res[l]
        l+=1
        r-=1

    return sum([int(x) * idx for idx, x in enumerate(res) if x != '.'])


if __name__ == '__main__':
    print(part1())
