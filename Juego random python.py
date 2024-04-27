import random 
ai = random.randint(1,10)
numero = -1
while numero != ai:
    numero = int(input("introduce un numero: "))
    if numero > ai:
        print("te has pasado")
    elif numero < ai:
        print("te has quedado corto")

print(f"Felicidades, el numero era {ai}")

