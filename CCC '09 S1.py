def binary_exponentiation(base, exponent):
    if exponent == 0:
        return 1 
    elif exponent == 1:
        return base
    else:
        split = binary_exponentiation(base, exponent//2)
        if exponent % 2 == 0:
            return (split * split) 
        else:
            return (split * split * base)

import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
cnt = 0
for i in range(1, 22):
    _pow = binary_exponentiation(i, 6)
    if _pow >= a and _pow <= b:
        cnt += 1 
    if _pow >= b:
        break
print(cnt)
