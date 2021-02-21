import sys
import math
n = int(sys.stdin.readline())
for x in range(n):
    number = int(sys.stdin.readline())
    list_sd = []
    for i in range(1, math.floor(number ** 0.5) + 1):
        if number % i == 0:
            factor2 = number // i
            list_sd.append(i + factor2)
            list_sd.append(abs(i - factor2))
    if len(list_sd) == len(set(list_sd)):
        print(str(number), "is not nasty")
    else:
        print(str(number), "is nasty")
