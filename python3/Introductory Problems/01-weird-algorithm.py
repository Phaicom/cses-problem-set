n = [int(x) for x in input().split()]


def weird(n: int):
    if n == 1:
        return "1"
    return str(int(n)) + " " + weird(n / 2 if n % 2 == 0 else (n * 3) + 1)


print(weird(n[0]))
