import collections

def part2():
    grid = [[char for char in line] for line in open('input.txt').read().split("\n")]
    ROWS,COLS = len(grid), len(grid[0])

    def bfs(row,col):
        queue = collections.deque([(row,col)])
        res = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == "9":
                    res += 1
                    continue
                adj = [(1,0), (-1,0), (0,1), (0,-1)]
                for dx,dy in adj:
                    newRow, newCol = r+dx, c + dy
                    if newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLS or int(grid[r][c]) != int(grid[newRow][newCol]) - 1:
                        continue
                    queue.append((newRow,newCol))
        return res


    return sum([bfs(i,j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == "0"])


if __name__ == '__main__':
    print(part2())
