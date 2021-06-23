def ad(s, i, su, total):
    if i == 0:
        return abs(total - su * 2)
    return min(ad(s, i - 1, su + s[i - 1], total), ad(s, i - 1, su, total))


n = int(input())
s = [int(i) for i in input().split(" ")]
print(ad(s, n, 0, sum(s)))
