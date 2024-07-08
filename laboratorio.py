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

def palabra_mas_repetida(frecuencias):
    palabra_mas_repetida = max(frecuencias, key=frecuencias.get)
    frecuencia_mas_repetida = frecuencias[palabra_mas_repetida]
    return palabra_mas_repetida, frecuencia_mas_repetida

cadena = input("Ingrese una cadena de caracteres: ")

frecuencias = contarPlbr(cadena)

print("Frecuencias de palabras:")
for palabra, frecuencia in frecuencias.items():
    print(f"{palabra}: {frecuencia}")

palabra_mas_repetida, frecuencia_mas_repetida = palabra_mas_repetida(frecuencias)

print(f"La palabra más repetida es '{palabra_mas_repetida}' con una frecuencia de {frecuencia_mas_repetida}")