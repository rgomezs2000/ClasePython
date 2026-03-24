carrito = ["pan", "leche", "huevos"]

productoNuevo = input("Que producto quieres agregar?")
productoNuevo = str(productoNuevo)
carrito.append(productoNuevo)

carrito[1] = "mantequilla"
i = 0

print("Tu carrito:")
while i < len(carrito):
    print(carrito[i])
    i = i + 1