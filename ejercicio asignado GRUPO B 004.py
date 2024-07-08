print("Ingrese numeros ganadores de la tinka (separado por coma): ")
numGanador = input()

if numGanador == "":       #    en caso de no añadir valores
    print("No ingresó ningún número. Intente de nuevo.")
else:           # en caso no cumpla las comas separadas
    numGanador = numGanador.split(",")

    for i in range(len(numGanador)):   
        try:
            numGanador[i] = int(numGanador[i])
        except ValueError:
            print("Error: El número", numGanador[i], "no es válido. Intente de nuevo.")
            exit()

    numGanador.sort()
    numGanador.reverse()

    print("Los números ganadores de la tinka son:")    
    for numero in numGanador:
        print(numero)