n = int(input())
lst1 = list(map(str, input().split()))
lst2 = list(map(str, input().split()))
bln_good = True
for j in range(n):
    init_name = lst1[j]
    bottom_name = lst2[j]
    index1 = lst1.index(bottom_name)
    if lst2[index1] != init_name or init_name == bottom_name:
        bln_good = False
        break
if (bln_good):
    print("good")
else:
    print("bad")
