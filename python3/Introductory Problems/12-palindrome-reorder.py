def palReorder(s):
    arr = {c: s.count(c) for c in set(s)}
    count = 0
    re = ""
    l = ""
    for i in arr:
        c = arr[i]
        if c % 2 == 1:
            l = i
            count += 1
        else:
            re = (i * (c // 2)) + re + (i * (c // 2))
    if count > 1:
        print("NO SOLUTION")
    else:
        if l:
            d = len(re) // 2
            re = re[:d] + l * arr[l] + re[d:]
            print(re)
        else:
            print(re)


palReorder(input())
