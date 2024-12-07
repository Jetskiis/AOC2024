def part1():
    input = [[char for char in line] for line in open('input.txt').read().split("\n")]
    ROWS, COLS = len(input), len(input[0])
    x, y = next(((i, j) for i in range(ROWS) for j in range(COLS) if input[i][j] == '^'))
    dx,dy = -1,0
    while True:
        newX, newY = x + dx, y + dy
        input[x][y] = 'X'
        if newX < 0 or newY < 0 or newX >= ROWS or newY >= COLS:
            break
        if input[newX][newY] == '#':
            dx,dy = dy,-dx
            newX, newY = x + dx, y+dy
        # print(x,y,newX,newY)
        x,y = newX,newY
    # print(*(x for x in input), sep="\n")
    return sum([1 for i in range(ROWS) for j in range(COLS) if input[i][j] == 'X'])

if __name__ == '__main__':
    print(part1())