def part2():
    input = [[char for char in line] for line in open('input.txt').read().split("\n")]
    ROWS, COLS = len(input), len(input[0])
    res = 0
    for i in range(ROWS):
        for j in range(COLS):
            x, y = next(((i, j) for i in range(ROWS) for j in range(COLS) if input[i][j] == '^'))
            if input[i][j] != '.':
                continue
            input[i][j] = '#'
            visit = set()
            dx,dy = -1,0
            while True:
                newX, newY = x + dx, y + dy
                if newX < 0 or newY < 0 or newX >= ROWS or newY >= COLS:
                    break
                while input[newX][newY] == '#':
                    dx,dy = dy,-dx
                    newX, newY = x + dx, y+dy
                if (x,y,newX,newY) in visit:
                    res += 1
                    break
                visit.add((x,y,newX,newY))
                x,y = newX,newY
            input[i][j] = '.'
    return res


if __name__ == '__main__':
    print(part2())