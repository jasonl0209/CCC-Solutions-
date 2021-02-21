counter = 0
n = int(input())
lst_1 = input().split(" ")
for k in range(n):
    lst_1[k] = int(lst_1[k])
lst_2 = input().split(" ")
for k in range(n):
    lst_2[k] = int(lst_2[k])
if question_n == 1:
    lst_1 = sorted(lst_1)
    lst_2 = sorted(lst_2)
    for j in range(n):
        counter+=max(lst_1[j], lst_2[j])
    print(counter)
else:
    for i in range(n):
        lst_1.append(lst_2[i])
    lst_1 = sorted(lst_1)
    for x in range(n, 2*n):
        counter+=lst_1[x]
    print(counter)
