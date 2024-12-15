from _collections import defaultdict

def part1():
    coord_to_val = defaultdict(str) | {(rowNum,colNum): col for rowNum,row in enumerate(open("input.txt")) for colNum, col
                               in enumerate(row)} #open file from stdin
    coords = list(coord_to_val.keys())
    val_to_coord = defaultdict(list) | {val: [(rowNum, colNum) for rowNum, colNum in coords if coord_to_val[(rowNum, colNum)] == val]
        for val in coord_to_val.values()}
    res = 0
    for val,coords in val_to_coord.items():
        if val.isalnum():
            for i in range(len(coords)):
                for j in range(i+1, len(coords)):
                    dx,dy = coords[i][0] - coords[j][0], coords[i][1] - coords[j][1]
                    leftX, leftY = coords[i][0] + dx, coords[i][1] + dy
                    rightX, rightY = coords[j][0] - dx, coords[j][1] - dy
                    for pair in [(leftX, leftY), (rightX, rightY)]:
                        if pair in coord_to_val and not coord_to_val[pair].isalnum():
                            res += 1
    return res



if __name__ == "__main__":
    print(part1())