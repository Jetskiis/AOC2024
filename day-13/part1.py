from parse import findall
from sympy import solve, Symbol, Eq

def part1():
    input = open('input.txt').read()
    res = 0
    for x1,y1,x2,y2,total1,total2 in findall("Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}", input):
        y = Symbol("y", integer=True)
        x = Symbol("x", integer=True)
        total1 += 1000000000000
        total2 += 1000000000000
        output = solve([x1*x + y1*y - total1, x2*x + y2*y - total2],[x,y])
        print(output)


if __name__ == "__main__":
    print(part1())