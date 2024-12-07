def part1():
    arr = [[char for char in line] for line in open('part1input.txt').read().splitlines()]
    # arr = [[char for char in line] for line in open('test.txt').read().splitlines()]
    ROWS, COLS = len(arr), len(arr[0])

    def dfs(row, col, i, prevX, prevY):
        if i == 4:
            return 1
        directions = [(row-1,col),(row+1,col),(row,col+1),(row,col-1),
               (row-1,col+1),(row-1,col-1),(row+1,col+1),(row+1,col-1)]
        res = 0
        if prevX == None and prevY == None:
            for x,y in directions:
                if x < 0 or y < 0 or x >= ROWS or y >= COLS or arr[x][y] != 'XMAS'[i]:
                    continue
                res += dfs(x,y,i+1,row,col)
            return res
        newX, newY = row + (row - prevX), col + (col - prevY)
        if newX < 0 or newY < 0 or newX >= ROWS or newY >= COLS or arr[newX][newY] != 'XMAS'[i]:
            return res
        res += dfs(newX, newY, i + 1, row,col)
        return res

    return sum([dfs(i,j,1,None,None) for i in range(ROWS) for j in range(COLS)
                if arr[i][j] == 'X'])

if __name__ == '__main__':
    print(part1())
