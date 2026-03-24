inventario = [
    {"nombre": "Avena", "precio": 2.50, "stock": 10},
    {"nombre": "Leche", "precio": 1.20, "stock": 20},
    {"nombre": "Pan", "precio": 0.50, "stock": 50},
]

print("Listando Inventario:")

for producto in inventario:
    lista = f"Producto: {producto['nombre']} | Precio: ${producto['precio']}"
    print(lista)