def contarPlbr(cadena):
    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def maxPalbraRepetid(frecuencias):
    maxPalbraRepetid = max(frecuencias, key=frecuencias.get)
    maxFrecnciRepetidd = frecuencias[maxPalbraRepetid]
    return maxPalbraRepetid, maxFrecnciRepetidd

cadena = input("Ingrese una cadena de caracteres: ")

frecuencias = contarPlbr(cadena)

print("Frecuencias de palabras:")
for palabra, frecuencia in frecuencias.items():
    print(f"{palabra}: {frecuencia}")

maxPalbraRepetid, maxFrecnciRepetidd = maxPalbraRepetid(frecuencias)

print(f"La palabra más repetida es '{maxPalbraRepetid}' con una frecuencia de {maxFrecnciRepetidd}")