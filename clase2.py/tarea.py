# Solicitar al usuario que ingrese dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar si los números son pares o impares
es_par1 = numero1 % 2 == 0
es_par2 = numero2 % 2 == 0

# Evaluar las combinaciones posibles
if es_par1 and es_par2:
    print("Ambos números son pares.")
elif not es_par1 and not es_par2:
    print("Ambos números son impares.")
else:
    print("Uno de los números es par y el otro es impar.")