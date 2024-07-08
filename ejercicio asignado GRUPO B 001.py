list1 = input("Ingrese palabras para lista 1 (separadas por coma): ").split(',')
list2 = input("Ingrese palabras para lista 2 (separadas por coma): ").split(',')

newList = []
for palabra in list1:
    palabra = palabra.strip()
    if palabra not in [p.strip() for p in list2]:
        newList.append(palabra)

print("vistaso de lista 1 despues de elimar palabras de lista 2:", newList)