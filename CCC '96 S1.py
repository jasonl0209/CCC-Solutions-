import sys
import math
num = int(sys.stdin.readline())
for x in range(num):
    n = int(sys.stdin.readline())    
    _sum = 1 
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            _sum += i 
            if i != n//i:
                _sum += n//i 
    if _sum < n:
        print(str(n) + " is a deficient number.")
    elif _sum > n:
        print(str(n) + " is an abundant number.")
    else:
        print(str(n) + " is a perfect number.")
