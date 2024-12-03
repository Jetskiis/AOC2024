import re

def part1():
    txt = open('part1input.txt','r').read()
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)',txt)
    res = 0
    # for match in matches:
    #     res += int(match[match.find("(") + 1:match.find(",")]) * int(match[match.find(",")+1:match.find(")")])
    return sum(int(match[match.find("(") + 1:match.find(",")]) * int(match[match.find(",")+1:match.find(")")]) for match in matches)
    # return res

if __name__ == '__main__':
    print(part1())
