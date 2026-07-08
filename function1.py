a = [8, 3, 5, 9, 2]
mayor = 0
menor = 99999
def encontrar_mayor(lista):
    global mayor
    for numero in lista:
        if numero > mayor:
            mayor = numero
    print("mayor", mayor)
encontrar_mayor(a)

def encontrar_menor(lista):
    global menor
    for numero in lista:
        if numero < menor:
            menor = numero
    print("menor", menor)
encontrar_menor(a)