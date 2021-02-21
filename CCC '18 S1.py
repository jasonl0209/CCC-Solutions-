n = int(input())
lst = []
lst2 = []
for g in range(n):
    th = input()
    lst.append(int(th))
lst = sorted(lst)
for i in range(1, n-1):
    lst2.append((lst[i] - lst[i-1])/2 + (lst[i+1] - lst[i])/2)
print(min(lst2))
