año = int(input("Introduce un año: "))
def bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False


if bisiesto(año):
    print(año, "es bisiesto")
else:
    print(año, "no es bisiesto")