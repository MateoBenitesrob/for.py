productos = {
    "laptop": 1200,
    "mouse": 80,
    "teclado": 150,
    "monitor": 900,
    "audifonos": 200
}
producto_caro = 0
valor_premiums = 0
nombre_del_producto_caro = ""
contador = 0
for producto in productos:
    print(producto, "cuesta", productos[producto], "doláres.")
    if productos[producto] >= 500:
        valor_premiums  += productos[producto]
        contador += 1
        if productos[producto] > producto_caro:
            producto_caro =  productos[producto]
            nombre_del_producto_caro = producto
    print("------------------------------------------")
print("hay", contador, "productos premium:")
print("el valor total de los productos premiums son de: ", valor_premiums, "doláres.")
print("Nuesto producto estrella es la", nombre_del_producto_caro, "con", producto_caro, "doláres." )