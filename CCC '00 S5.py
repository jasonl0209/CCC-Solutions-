n = int(input())
lst = []
lst2 = []
minimum = 1200.00
for j in range(2*n):
    inp = float(input())
    lst.append(inp)
    if j%2 == 1:
        if inp < minimum:
            minimum = inp
for x in range(1, 2*n+1, 2):
    if lst[x] == minimum:
        lst2.append(lst[x-1])
for i in lst2:
    if i%1 == 0 and minimum%1 == 0:
        print("The sheep at ("+str(i)+"0, "+str(minimum)+"0)", "might be eaten.")
    elif i%1 == 0:
        print("The sheep at ("+str(i)+"0, "+str(minimum)+")", "might be eaten.")
    elif minimum%1 == 0:
        print("The sheep at ("+str(i)+", "+str(minimum)+"0)", "might be eaten.")
    else:
        print("The sheep at ("+str(i)+", "+str(minimum)+")", "might be eaten.")
