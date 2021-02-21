data_sets = int(input())
for i in range(data_sets):
    list_of_subjects = []
    list_of_verbs = []
    list_of_objects = []
    number_of_subjects = int(input())
    number_of_verbs = int(input())
    number_of_objects = int(input())
    for a in range(number_of_subjects):
        list_of_subjects.append(input())
    for q in range(number_of_verbs):
        list_of_verbs.append(input())
    for y in range(number_of_objects):
        list_of_objects.append(input())
    for e in list_of_subjects:
        for l in list_of_verbs:
            for j in list_of_objects:
                print(e+' '+l+' '+j+'.')
