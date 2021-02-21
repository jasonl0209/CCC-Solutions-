str1 = input()
str2 = input()
if len(str1) != len(str2):
    print("N")
else:
    astericks = str2.count("*")
    #if astericks == 0:
      #  print("N")
    #else:
    counter = 0
    lst1, lst2 = [], []
    for letter in str1:
        lst1.append(letter)
    for char in str2:
        lst2.append(char)
    for x in lst1:
        if lst2.count(x) > 0:
            lst2.remove(x)
        else:
            counter += 1
    if len(lst2) == astericks:
        if astericks == counter:
            print("A")
        else:
            print("N")
    else:
        print("N")
