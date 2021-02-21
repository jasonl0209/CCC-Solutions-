number = int(input())
lst = []
for i in range(number):
    string = ''
    for s in input():
        if s.isalpha() == True:
            if s=="A" or s=="B" or s=="C":
                s = 2
            elif s=="D" or s=="E" or s=="F":
                s = 3
            elif s=="G" or s=="H" or s=="I":
                s = 4
            elif s=="J" or s=="K" or s=="L":
                s = 5
            elif s=="M" or s=="N" or s=="O":
                s = 6
            elif s=="P" or s=="Q" or s=="R" or s=="S":
                s = 7
            elif s=="T" or s=="U" or s=="V":
                s = 8
            else:
                s = 9
        if s!="-":
            string = string+str(s)
    lst.append(string)
for io in lst:
    print(io[:3]+"-"+io[3:6]+"-"+io[6:10])
