import sys
n = int(sys.stdin.readline())
lst_inp = []
lst_val = []
for i in range(n):
    str_input, r, s, d = map(str, sys.stdin.readline().split())
    val = 2 * int(r) + 3 * int(s) + int(d) 
    lst_inp.append(str_input)
    lst_val.append(val)
if n > 0:
    max_val = max(lst_val)
    if lst_val.count(max_val) == 1:
        print(lst_inp[lst_val.index(max_val)])
        lst_val[lst_val.index(max_val)] = 0
        if n > 1:
            max2 = max(lst_val)
            print(lst_inp[lst_val.index(max2)])
    else:
        str1 = lst_inp[lst_val.index(max_val)]
        lst_val[lst_val.index(max_val)] = 0
        max2 = max(lst_val)
        str2 = lst_inp[lst_val.index(max_val)]
        lst = []
        lst.append(str1)
        lst.append(str2)
        lst.sort()
        print(lst[0])
        print(lst[1])
