def monto_final():
    sinIGV = float(input("ingrese monto sin IGV: "))
    porcentajeIGV = float(input("ingrese porcentaje de IGV: ") or 12)
    return sinIGV + sinIGV * (porcentajeIGV / 100)

finalMount = monto_final()
print("El total de la factura es:", finalMount,"$")