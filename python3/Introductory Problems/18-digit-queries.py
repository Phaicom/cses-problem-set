import sys


def dq(n):
    l = f = 1
    while n > 9 * f * l:
        n -= 9 * f * l
        l += 1
        f *= 10
    q, r = divmod(n - 1, l)
    return str(f + q)[r]


def solution():
    re = []
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        re.append(dq(n))
    print("\n".join(str(i) for i in re))


solution()

# Explanation:
# if n = 191, n stand for nth of 1 to m concatenate string while m = 1000 according to cses problem
# before following the next step,
# We can divided set of number by length of its contained index
# eg: set 1 contain 1 index such as 5 = [5:5], 9 = [9:9]
# eg: set 2 contain 2 index such as 15 = [1:19, 5:20], 30 = [3:49, 0:50]
# and so on
# l = set that contain nth, f = first value of set l
# n is in set 3, So l = 3, f = 1 * 10**(l-1) = 100
# next, we have to minus n with total number of set 1+2,
# so that we can have remaining nth of set 3
# number of set 1 = 9*1*1 = 9
# number of set 2 = 9*2*10 = 180
# n = 190-(9+180) = 2, 2 is nth in set 3
# find q, fq and r
# remark!: n-1 is for converting nth into index (index of set l is n-1)
# q = (n-1)//l = (2-1)//3 = 1//3 = 0, Its mean index of 1 in set 3 is no additional value
# //3 mean number in set 3 consist of 3 index eg: 100 = [1:189, 0: 190, 0: 191]
# that why we divided index by 3, so that we can know what exacly is additional value
# apart from first value(aka. start number)
# take a look at example below
# if nth of set 3 is 1,2 or 3, after we convert it into index and divided by length of its set
# result still be the same for all nth above
# : (1-1)//3 = 0, (2-1)//3 = 0, (3-1)//3 = 0
# So either  1, 2 or 3 nth still on the same number because it have the same additional value
# fq is simple, we add additional value to first value. that's it!
# now we have the number of index n-1 in set l equal to 100
# fq = f+q = 100 + 0 = 100
# for this spot. we known 191th is on set 3
# Somewhere in number 100
# What is missing is index of 191th in number 100 right?
# From what we known. set 3 consist of 3 index if we modular index of set l by l.
# we can know what index of fq is.
# r = (n-1)%l = (2-1)%3 = 1
# result will be -> index r of string(number fq)
# fq = 100: number
# r  = 1  : index
# result = str(fq)[r] = ["1","0"."0"][1] = 0
