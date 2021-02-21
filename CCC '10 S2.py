n = int(input())
lst_letter = []
lst_code = []
out = ""
Min = 10000000000000000000000000000000000000000000000000000000000000000000
for i in range(n):
    a, b = map(str, input().split())
    lst_letter.append(a)
    lst_code.append(b)
    l = len(b)
    if l < Min:
        Min = l
string = input()
while len(string) > 0:
    temp = string[:Min]
    x = Min
    while lst_code.count(temp) == 0:
        temp += string[x]
        x += 1 
    out += lst_letter[lst_code.index(temp)]
    string = string[x:]
print(out)
