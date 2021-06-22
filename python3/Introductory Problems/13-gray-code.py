def solution(n):
    l1 = ["0", "1"]
    for i in range(n - 1):
        l2 = ["1" + i for i in l1[::-1]]
        l1 = ["0" + i for i in l1]
        l1 = l1 + l2
    print("\n".join(l1))


solution(int(input()))
