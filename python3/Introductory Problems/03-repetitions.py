def getRepet(dnas):
    cur = ""
    cumu = 0
    max = 0
    for dna in dnas:
        if dna == cur:
            cumu += 1
        else:
            cumu = 1
            cur = dna
        if cumu > max:
            max = cumu
    return max


print(getRepet(input()))
