with open("input.txt", "r") as file:
    lista = []
    for lines in file:
        lines = lines.rstrip()
        lista.append(lines)
    sortowane = sorted(lista)
    for i in range(0, len(sortowane)):
        print(sortowane[i], "\n")