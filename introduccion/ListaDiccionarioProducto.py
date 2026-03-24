inventario = [
    {"nombre": "Avena", "precio": 2.50, "stock": 10},
    {"nombre": "Mantequilla", "precio": 1.80, "stock": 15},
    {"nombre": "Leche", "precio": 1.20, "stock": 20},
    {"nombre": "Huevos", "precio": 1.00, "stock": 25},
    {"nombre": "Pan", "precio": 0.50, "stock": 50},
    {"nombre": "Papas", "precio": 0.60, "stock": 100}
]
i = 0

def calcularPrecioIVA(precio):
    total = precio * 1.16
    return total

def generarFactura():
    totalFinal = 0
    for producto in inventario:
        totalFinal += calcularPrecioIVA(producto["precio"])
    return totalFinal

factura = generarFactura()
print(f"Total a pagar: ${factura}")