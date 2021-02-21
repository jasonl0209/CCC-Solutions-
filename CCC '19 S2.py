import math
n = int(input())
lst = []
lst_out = []
for kyt in range(n):
    ger = int(input())
    lst.append(ger)
for i in lst:
    bln_composite = False
    bln_second = False
    if i % 2 != 0:
        for t in range(3, math.floor(i ** 0.5) + 1, 2):
            if i % t == 0:
                bln_composite = True
                break
    else:
        bln_composite = True
    if bln_composite == False:
        lst_out.append(i)
        lst_out.append(i)
    else:
        if i % 2 == 0:
            for h in range(1, i - 2, 2):
                bln_composite2 = False
                bln_composite3 = False
                for p in range(3, math.floor((i + h) ** 0.5) + 1, 2):
                    if (i + h) % p == 0:
                        bln_composite2 = True
                        break
                if bln_composite2 == False:
                        for q in range(3, math.floor((i - h) ** 0.5) + 1, 2):
                            if (i - h) % q == 0:
                                bln_composite3 = True
                                break
                if bln_composite2 == False and bln_composite3 == False:
                        lst_out.append(i - h)
                        lst_out.append(i + h)
                        break
        else:
            for b in range(2, i - 2, 2):
                bln_composite2B = False
                bln_composite3B = False
                for c in range(3, math.floor((i + b) ** 0.5) + 1, 2):
                    if (i + b) % c == 0:
                        bln_composite2B = True
                        break
                if bln_composite2B == False:
                    for d in range(3, math.floor((i - b) ** 0.5) + 1, 2):
                        if (i - b) % d == 0:
                            bln_composite3B = True
                            break
                if bln_composite2B == False and bln_composite3B == False:
                    lst_out.append(i - b)
                    lst_out.append(i + b)
                    break

for jh in range(n):
    print(lst_out[jh*2], lst_out[(jh*2)+1])
