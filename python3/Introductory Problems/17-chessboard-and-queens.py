import sys

re = [0]


def checkQ(b, r, c):
    for i in range(c):
        if b[r][i] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if b[i][j] == 1:
            return False
    for i, j in zip(range(r, 8, 1), range(c, -1, -1)):
        if b[i][j] == 1:
            return False
    return True


def NQ(b, c, n):
    if c == n:
        re[0] += 1
        return

    for r in range(n):
        if checkQ(b, r, c) and b[r][c] != -1:
            b[r][c] = 1
            NQ(b, c + 1, n)
            b[r][c] = 0 if b[r][c] == 1 else b[r][c]


def solution(n):
    b = []
    for i in range(8):
        b.append([0 if j == "." else -1 for j in sys.stdin.readline().strip()])
    NQ(b, 0, n)
    print(re[0])


solution(8)
