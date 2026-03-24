producto = {
    "nombre": "Avena Eduardo",
    "precio": 2.50,
    "stock": 100
}

nombre = producto["nombre"]

cantidad = input(f"Cuantos quieres de {producto['nombre']}?")
cantidad = int(cantidad)

precio = producto["precio"]

total = precio * cantidad
total = float(total)


stock = producto["stock"]

producto["stock"] = stock - cantidad
stock = producto["stock"]

mensaje = f"Compra exitosa de {nombre}.\nTotal: ${total}.\nQuedan: {stock} en stock."
print(mensaje)