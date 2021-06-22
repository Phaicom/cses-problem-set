result = []


def toh(n, l, r, m):
    if n == 1:
        result.append(l + " " + r)
        return
    toh(n - 1, l, m, r)
    result.append(l + " " + r)
    toh(n - 1, m, r, l)


toh(int(input()), "1", "3", "2")
print(len(result))
print("\n".join(result))
