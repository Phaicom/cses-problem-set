import sys

l, a = map(lambda x: list(map(int, x.split())), sys.stdin.readlines())


def incArr():
    move = 0
    for i in range(l[0] - 1):
        dif = a[i] - a[i + 1]
        if dif > 0:
            a[i + 1] += dif
            move += dif
    return move


print(incArr())
