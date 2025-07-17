# Definimos las funciones matemáticas

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir por cero"

# Probamos las funciones con números de ejemplo
num1 = 10
num2 = 5

print("Número 1:", num1)
print("Número 2:", num2)

print("\nResultados:")
print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))
print("Multiplicación:", multiplicar(num1, num2))
print("División:", dividir(num1, num2))
