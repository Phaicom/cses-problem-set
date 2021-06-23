# solution 1 pure python
result = set()


def cs(l, r):
    if len(r) == 1:
        return
    result.add("".join(l + r))
    result.add("".join(l + r[::-1]))
    for i in range(len(r)):
        cs(l + r[:1], r[1:])
        r = r[1:] + r[:1]


s = [i for i in input()]
for i in range(len(s)):
    cs(s[:1], s[1:])
    s = s[1:] + s[:1]
print(len(result))
print("\n".join(sorted(result)))


# solution 2 itertools
from itertools import permutations

s = input()
result = sorted({"".join(i) for i in permutations(s, len(s))})
print(len(result))
print("\n".join(result))
