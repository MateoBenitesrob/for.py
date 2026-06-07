jugadores = {
            "mateo": 250,
             "alex": 180,
             "sofia": 320,
             "lukas": 90,
             "maria": 210
}

mejor_jugador = ""
mayor_puntos = 0
puntos_mínimo = 999999
peor_jugador = ""
total = 0
promedio = 0
for jugador in jugadores:


    if jugadores[jugador] > mayor_puntos:
        mayor_puntos = jugadores[jugador]
        mejor_jugador = jugador

    if jugadores[jugador] < puntos_mínimo:
        puntos_mínimo = jugadores[jugador]
        peor_jugador = jugador
    total += jugadores[jugador]
promedio = total / 5

for jugador in jugadores:


    if jugadores[jugador] >= promedio:
        print(jugador, "tiene más del promedio")
        print("---------------------------")
        
    elif jugadores[jugador] < promedio:
        print(jugador, "tiene menos del promedio")
        print("---------------------------")
    
print(mejor_jugador, "es la jugadora con más puntos:",mayor_puntos)
print(peor_jugador,"es el jugador con menos puntos:", puntos_mínimo)
print("el total de puntos recaudados fueron", total, "puntos")
