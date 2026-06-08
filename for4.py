ventas = {"minecraft": 15,
          "roblox premium": 8,
          "fortinite pass": 20,
          "among us": 15,
          "terraria": 12
}
venta_diez = 10
productos_conventas = 0
total_ventas = 0
producto_másvendido = ""
promedio = 0
productoventas = 0
for venta in ventas:
    print("se vendieron", ventas[venta], "productos de", venta)
    if ventas[venta] >= venta_diez:
        productos_conventas += 1
    total_ventas += ventas[venta]
    if ventas[venta] > productoventas:
        productoventas = ventas[venta]
        producto_másvendido = venta
promedio = total_ventas / 5
for venta in ventas:
    if ventas[venta] >= promedio:
        print("el producto", venta, "esta por encima del promedio de ventas.")
        print("--------------------")
    elif ventas[venta] < promedio:
        print("el producto", venta, "esta por debajo del promedio de ventas.")
        print("--------------------")
print("el producto más vendido es:", producto_másvendido, "con", productoventas, "ventas")
print("el total de ventas fueron de:", total_ventas)