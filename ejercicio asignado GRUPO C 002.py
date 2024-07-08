facturas = {}
cobrada = 0
pendiente = 0

while True:
    print("1. Añadir factura\n2. Pagar factura\n3. Terminar")
    o = input("Seleccione una opción: ")
    if o == "1":
        n = input("Número de factura: ")
        c = float(input("Coste: "))
        facturas[n] = c
        pendiente += c
    elif o == "2":
        n = input("Número de factura a pagar: ")
        if n in facturas:
            c = facturas[n]
            del facturas[n]
            cobrada += c * 1.18
            pendiente -= c
        else:
            print("Factura no encontrada")
    elif o == "3":
        break
    else:
        print("Opción no valida intente de nuevo")
    print("Cobrada:", cobrada, "\nPendiente:", pendiente)