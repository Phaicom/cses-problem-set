import sys


def tk(ns):
    for n in range(1, ns + 1):
        print(int(((n ** 4) - (9 * (n ** 2)) + (24 * n) - 16) / 2))


tk(int(sys.stdin.readline()))
