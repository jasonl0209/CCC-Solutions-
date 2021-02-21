number = int(input())
t = 0
s = 0
for i in range(number):
    string = input()
    s = s + string.count('s') + string.count('S')
    t = t + string.count('t') + string.count('T')
if t>s:
    print('English')
else:
    print('French')
