import sys

l, ns = map(lambda x: list(map(int, x.split())), sys.stdin.readlines())
total = l[0] * (l[0] + 1) / 2
print(int(total - sum(ns)))
