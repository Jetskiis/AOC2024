import re

def part2():
    txt = open('part1input.txt','r').read()
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)',txt)
    res = 0
    yes = True
    for match in matches:
        if match == 'do()':
            yes = True
        elif match == 'don\'t()':
            yes = False
        elif yes:
            res += int(match[match.find("(") + 1:match.find(",")]) * int(match[match.find(",")+1:match.find(")")])
    return res

if __name__ == '__main__':
    print(part2())
