try:
    numero = int(input("Coloque tu numero:\n"))
    resultado = 10 / numero
    print(f"El resultado es: {numero}")
except ValueError:
    print("Debes ingresar un numero, no letras.")
except ZeroDivisionError:
    print("Error! No se puede dividir entre ceros.")
except Exception as ex:
    print(f"HA ocurrido un error: {ex}")
