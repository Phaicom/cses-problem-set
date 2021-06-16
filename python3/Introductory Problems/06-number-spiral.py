import sys

for i in range(int(sys.stdin.readline())):
    row, col = [int(j) for j in sys.stdin.readline().split()]
    if row >= col:
        print((row ** 2) - (col - 1) if row % 2 == 0 else ((row - 1) ** 2) + col)
    else:
        print((col ** 2) - (row - 1) if col % 2 != 0 else ((col - 1) ** 2) + row)
