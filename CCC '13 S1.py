first = int(input())
bln_true = 0
while bln_true == 0:
    first+=1
    string_first = str(first)
    if string_first.count('0')<=1 and string_first.count('1')<=1 and string_first.count('2')<=1 and string_first.count('3')<=1 and string_first.count('4')<=1 and string_first.count('5')<=1 and string_first.count('6')<=1 and string_first.count('7')<=1 and string_first.count('8')<=1 and string_first.count('9')<=1:
        bln_true = 1
        print(first)
