import sys


def cp(a, b):
    if (a + b) % 3 == 0 and 2 * a >= b and 2 * b >= a:
        print("YES")
    else:
        print("NO")


for i in range(int(sys.stdin.readline())):
    l, r = [int(j) for j in sys.stdin.readline().split()]
    cp(l, r)
