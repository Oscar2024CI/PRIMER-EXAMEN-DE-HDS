carrito = {}

while True:
    print("Ingrese el artículo y su precio (separados por espacio), o escriba 'terminar' para finalizar: ")
    articulo_precio = input().split()

    if articulo_precio[0] == "terminar":
        break

    articulo = articulo_precio[0]
    precio = float(articulo_precio[1])

    carrito[articulo] = precio

print("Lista de la compra:")
for articulo, precio in carrito.items():
    print(articulo, "-", precio)

print("Costo total:", sum(carrito.values()))