def per(l):
    if l == 2 or l == 3:
        return "NO SOLUTION"
    res = list(range(l - 1, 0, -2))
    res += list(range(l, 0, -2))
    return " ".join(str(i) for i in res)


print(per(int(input())))
