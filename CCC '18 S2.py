import sys
n = int(sys.stdin.readline())
list_input = []
for i in range(n):
    inp = list(map(int, sys.stdin.readline().split()))
    list_input.append(inp)
    
list_min = [list_input[0][0], list_input[0][n - 1], list_input[n - 1][0], list_input[n - 1][n - 1]]
minimum = min(list_min)
if minimum == list_input[0][0]:
    for i in range(n):
        print(*list_input[i])
        
elif minimum == list_input[0][n - 1]:
    for i in range(n - 1, -1, -1):
        list_temp = []
        for j in range(n): 
            list_temp.append(list_input[j][i])
        print(*list_temp)
            
elif minimum == list_input[n - 1][0]:
    for i in range(n):
        list_temp = []
        for j in range(n - 1, -1, -1):
            list_temp.append(list_input[j][i])
        print(*list_temp)
    
else:
    for i in range(n - 1, -1, -1):
        list_temp = []
        for j in range(n - 1, -1, -1):
            list_temp.append(list_input[i][j])
        print(*list_temp)
