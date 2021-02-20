import sys
quarters = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
cnt = 0

while quarters > 0:
    a += 1 
    if quarters > 0:
        quarters -= 1 
        cnt += 1
        if a % 35 == 0:
            quarters += 30
            
    b += 1 
    if quarters > 0:
        quarters -= 1 
        cnt += 1
        if b % 100 == 0:
            quarters += 60
            
    c += 1 
    if quarters > 0:
        quarters -= 1 
        cnt += 1
        if c % 10 == 0:
            quarters += 9

if cnt == 1:
    print("Martha plays " + str(cnt) + " time before going broke.")
else:
    print("Martha plays " + str(cnt) + " times before going broke.")
