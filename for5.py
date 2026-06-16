unalista = [12, 5, 18, 7, 20, 9, 15]
promedio = 0
total = 0
contadordemayores = 0
for numero in unalista:
    total += numero
promedio = total / 7
promedio = round(promedio, 2)

for numero in unalista:
    if numero > promedio:
        contadordemayores += 1
        print(numero, "es mayor al promedio")
        print("................................")
print("hay", contadordemayores, "números mayores del promedio:", promedio)