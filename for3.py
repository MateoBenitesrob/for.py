misiones = {"bosque": True,
            "cueva": False,
            "castillo": True,
            "montaña": False,
            "volcan": True}
misiones_completadas = 0
misiones_faltantes = 0
porcentaje = 0
total_misiones = 0

for mision in misiones:
    if misiones[mision] == True:
        print("la misión de", mision,"esta completada")
        print("-------------------------")
    elif misiones[mision] == False:
        print(mision, "esta pendiente")
        print("-------------------------")

    if misiones[mision] == True:
        misiones_completadas += 1
    elif misiones[mision] == False:
        misiones_faltantes += 1
    total_misiones += 1
porcentaje = misiones_completadas / total_misiones * 100

print("hay", misiones_completadas, "misiones completadas")
print("hay", misiones_faltantes, "misiones faltantes.")
print("tu progreso es de", porcentaje, "%")