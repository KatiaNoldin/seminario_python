# Lista inicial de deportes
deportes = ["Básquet", "Fútbol", "Vóley", "Tenis", "Natación"]

# Agregar más deportes
deportes.append("Handball")
deportes.append("Atletismo")
deportes.append("Rugby")

# Eliminar un deporte
deportes.remove("Tenis")

# Ordenar la lista alfabéticamente
deportes.sort()

# Mostrar todos los deportes con número
print("Lista de deportes disponibles:")
for i in range(len(deportes)):
    print(f"{i+1}. {deportes[i]}")

# Buscar un deporte específico
buscar = "Fútbol"
if buscar in deportes:
    print(f"\n¡{buscar} está en la lista de deportes!")
else:
    print(f"\n{buscar} no está en la lista.")

# Mostrar el total de deportes
print("\nCantidad total de deportes en la lista:", len(deportes))
