def part2():
    arr = [[char for char in line] for line in open('part1input.txt').read().splitlines()]
    # arr = [[char for char in line] for line in open('test.txt').read().splitlines()]
    ROWS, COLS = len(arr), len(arr[0])

    def dfs(row, col):
        positive = [(row-1,col+1), (row+1,col-1)]
        negative = [(row+1,col+1), (row-1,col-1)]
        for x,y in positive + negative:
            if x < 0 or y < 0 or x >= ROWS or y >= COLS:
                return 0
        return 0 if set([arr[positive[0][0]][positive[0][1]], arr[positive[1][0]][positive[1][1]]]) != set(["M","S"]) or set([arr[negative[0][0]][negative[0][1]], arr[negative[1][0]][negative[1][1]]]) != set(["M","S"]) else 1

    return sum([dfs(i,j) for i in range(ROWS) for j in range(COLS)
                if arr[i][j] == 'A'])

if __name__ == '__main__':
    print(part2())
