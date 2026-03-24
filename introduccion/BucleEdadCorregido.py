while True:
    edad_actual = input("Cual es tu edad? (puedes escribir 999 para abortar)")
    edad_actual = int(edad_actual)

    if edad_actual == 999:
        print("Gracias por participar! Adios!")
        break #Se va del bucle
    else:
        print("no puedo parar!!!!!")
    
    if edad_actual < 0:
        print("Viene del futuro")
    elif 0 <= edad_actual <= 12:
        print("Eres un niño!")
    elif 13 <= edad_actual <= 17:
        print("Eres un adolescente!")
    else:
        print("Eres un adulto")
    
    print("-" * 20)