def part2():
    lines = [[token for token in line.split(":") ] for line in open('input.txt').read().split("\n")]
    def dfs(target,array, index, cur):
        if index >= len(array) or cur > target:
            return cur if target == cur else 0
        if index == 0:
            return dfs(target,array, 1, int(array[0]))
        return max(dfs(target,array, index + 1, cur + int(array[index])), dfs(target, array, index + 1,
                                                                         cur * int(array[index])),
                   dfs(target,array,index+1,int(str(cur)+array[index])))
    return sum([dfs(int(line[0]), line[1].split(" ")[1:],0, 0) for line in lines])




if __name__ == '__main__':
    print(part2())