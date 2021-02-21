rawinput = input()
original = [1,2,3,4]
for i in range(len(rawinput)):
    if rawinput[i] == "H":
        original = [original[2], original[3], original[0], original[1]]
    elif rawinput[i] == "V":
        original = [original[1], original[0], original[3], original[2]]
print(original[0], original[1])
print(original[2], original[3])
