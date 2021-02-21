n = int(input())
lst = []
counter = 0
for x in range(2*n):
    lst.append(input())
for i in range(n):
    if lst[i] == lst[i+n]:
        counter+=1
print(counter)
