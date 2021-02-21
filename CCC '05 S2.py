import sys
a = 1
b = 1
x = 0 
y = 0
bx, by = map(int, sys.stdin.readline().split())
while a != 0 or b != 0:
    a, b = map(int, sys.stdin.readline().split())
    if x + a >= 0 and x + a <= bx:
        x += a
    else:
        if x + a < 0:
            x = 0 
        else:
            x = bx 
            
    if y + b >= 0 and y + b <= by:
        y += b
    else:
        if y + b < 0:
            y = 0 
        else:
            y = by 
            
    if a != 0 or b!= 0:    
        print(x, y)
