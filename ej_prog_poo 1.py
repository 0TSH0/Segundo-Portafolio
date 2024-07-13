# Dados los siguientes problemas de programación orientada a objetos seleccione uno e implemente una clase que cumpla lo que se pide (archivo .py o enlace de prueba en línea) NO TEXTO. 
# 1.- Diseñe una clase que represente un triángulo rectángulo y permita determinar el área, el perímetro, la hipotenusa y los ángulos de este a partir de sus dos catetos. Ejemplo: 
# Entrada: 	3, 4 
 
# Salida: 	Área:6 
#  	 	Perímetro: 12  	 	Hipotenusa 5 
 
# 	 	Ángulo 1: 53.13° 
#  	 	Ángulo 2: 36.86° 

import math

class TrianguloRectangulo:
    def __init__(self, cateto_a, cateto_b):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b
        self.hipotenusa = self.calcular_hipotenusa()
        self.angulo_a = self.calcular_angulo_a()
        self.angulo_b = self.calcular_angulo_b()

    def calcular_hipotenusa(self):
        return math.sqrt(self.cateto_a**2 + self.cateto_b**2)

    def calcular_area(self):
        return (self.cateto_a * self.cateto_b) / 2

    def calcular_perimetro(self):
        return self.cateto_a + self.cateto_b + self.hipotenusa

    def calcular_angulo_a(self):
        return math.degrees(math.atan(self.cateto_a / self.cateto_b))

    def calcular_angulo_b(self):
        return math.degrees(math.atan(self.cateto_b / self.cateto_a))

    def ver_res(self):
        print(f"Cateto A: {self.cateto_a}")
        print(f"Cateto B: {self.cateto_b}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")
        print(f"Hipotenusa: {self.hipotenusa}")
        print(f"Ángulo A (opuesto a cateto A): {self.angulo_a:.2f} grados")
        print(f"Ángulo B (opuesto a cateto B): {self.angulo_b:.2f} grados")

# Entrada desde la consola:
cateto_a = float(input("Introduce el valor del primer cateto: "))
cateto_b = float(input("Introduce el valor del segundo cateto: "))

triangulo = TrianguloRectangulo(cateto_a, cateto_b)
triangulo.ver_res()
