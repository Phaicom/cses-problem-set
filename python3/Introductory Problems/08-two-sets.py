def r(sta, sto, l):
    a = list()
    for i in range(sta, sto, 2):
        a.append(l[i - 1])
        a.append(l[-i])
    return a


def ts(n):
    if n % 4 not in [0, 3]:
        print("NO")
        return
    l = list(range(1, n + 1))
    a = list()
    b = list()
    if n % 4 == 3:
        l = list(range(4, n + 1))
        a = [1, 2]
        b = [3]
    a += r(1, int(len(l) / 2) + 1, l)
    b += r(2, int(len(l) / 2) + 1, l)
    print("YES")
    print(len(a))
    print(" ".join([str(i) for i in a]))
    print(len(b))
    print(" ".join([str(i) for i in b]))


ts(int(input()))
