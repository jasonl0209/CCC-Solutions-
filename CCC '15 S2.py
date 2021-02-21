import sys
j = int(sys.stdin.readline())
a = int(sys.stdin.readline())
lst_j = []
lst_size = []
lst_num = []
for i in range(j):
    s = sys.stdin.readline()
    if s == "S\n":
        lst_j.append(1)
    elif s == "M\n":
        lst_j.append(2)
    else:
        lst_j.append(3)

for i in range(a):
    x, y = map(str, sys.stdin.readline().split())
    if x == "S":
        lst_size.append(1)
    elif x == "M":
        lst_size.append(2)
    else:
        lst_size.append(3)
    lst_num.append(int(y))
    
lst_num, lst_size = (list(x) for x in zip(*sorted(zip(lst_num, lst_size)))) 
cnt = 0
i = 0
for num in lst_num:
    if lst_size[i] <= lst_j[num - 1]:
        cnt += 1
        lst_j[num - 1] = 0
    i += 1
print(cnt)
