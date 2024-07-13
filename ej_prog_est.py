# 1.- Diseñe una solución que convierte cualquier número romano a decimal. Ejemplo: 
# Entrada: XXXIV
# Salida: 34

print("//////////////////////////////////////1////////////////////////////////////////////")

def conversor(romano):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(romano):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

entrada = input("Introduce un número romano: ")
salida = conversor(entrada)
print(f"Entrada: {entrada}\nSalida: {salida}")

print("//////////////////////////////////////2////////////////////////////////////////////")

# 2.- Diseñe una solución que determine si una cadena de paréntesis, llaves y corchetes 
# es válida. Ejemplo: 
# Entrada: (){[]()} 
# Salida: Válido 

def verif(s):
    corchetes = []
    cadena = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in cadena.values():
            corchetes.append(char)
        elif char in cadena.keys():
            if corchetes == [] or cadena[char] != corchetes.pop():
                return False
        else:
            return False
    

    return corchetes == []


entrada = input("Introduce una cadena de paréntesis, llaves y corchetes: ")
salida = verif(entrada)
print(f"Entrada: {entrada}\nSalida: {'Válido' if salida else 'Inválido'}")

print("//////////////////////////////////////3////////////////////////////////////////////")

# 3.- Diseñe una solución que a partir de una lista de números retorne la cantidad de 
# números primos que contiene la misma. 
# Entrada: [2, 8, 10, 15, 13, 29, 50, 149] 
# Salida: 4 

def n_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def contador(nums):
    return sum(1 for num in nums if n_primo(num))

# Entrada desde la consola:
entrada = input("Introduce una lista de números separados por comas: ")
numeros = list(map(int, entrada.split(',')))
salida = contador(numeros)
print(f"Entrada: {numeros}\nSalida: {salida}")

print("//////////////////////////////////////4////////////////////////////////////////////")

# 4.- Diseñe una solución que a partir de una lista de calificaciones retorne una lista 
# con su valor equivalente en letras. 
# Entrada: [92, 68, 77, 75, 82] 
# Salida: [A, D, C, C, B] 


def nota_conversor(calificacion):
    if calificacion >= 90:
        return 'A'
    elif calificacion >= 80:
        return 'B'
    elif calificacion >= 70:
        return 'C'
    elif calificacion >= 60:
        return 'D'
    else:
        return 'F'

def calificacion(total):
    return [nota_conversor(grade) for grade in total]
entrada = input("Introduce una lista de calificaciones separadas por comas: ")
calificaciones = list(map(int, entrada.split(',')))
salida = calificacion(calificaciones)
print(f"Entrada: {calificaciones}\nSalida: {salida}")

print("//////////////////////////////////////5////////////////////////////////////////////")

# 5.- Diseñe una solución que a partir de una lista de palabras retorne otra lista 
# conteniendo únicamente las que son palíndromos. 
# Entrada: [“agua”, “rotor”, “perla”, “reconocer”, “ojo”, “peso”] 

# Salida: [“rotor”, “reconocer”, “ojo”]

def palidromo(palabra):
    return palabra == palabra[::-1]

def verificar(palabras):
    return [palabras for palabras in palabras if palidromo(palabras)]

# al momento de ingresar una palabra que sea un palídromo, trata de colocar todo el texto en mayusculas o minusculas
entrada = input("Introduce una lista de palabras separadas por comas: ")
palabras = [palabra.strip() for palabra in entrada.split(',')]
salida = verificar(palabras)
print(f"Entrada: {palabras}\nSalida: {salida}")
