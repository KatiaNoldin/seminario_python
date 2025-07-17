# Este programa verifica si un número es positivo, negativo o cero

# Pedimos al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Usamos condicionales para evaluar el número
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")