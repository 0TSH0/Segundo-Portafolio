# 2.- Diseñe una clase que represente una esfera y permita determinar el área de la superficie, el volumen y el diámetro a partir del radio. Ejemplo: 
# Entrada: 	5 
 # Salida: 	Área de la superficie: 314.16 
# Volumen: 523.6 Diámetro: 10 


import math

class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area_superficie(self):
        return 4 * math.pi * self.radio**2

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio**3

    def calcular_diametro(self):
        return 2 * self.radio

    def res(self):
        area_superficie = self.calcular_area_superficie()
        volumen = self.calcular_volumen()
        diametro = self.calcular_diametro()

        print(f"Radio: {self.radio}")
        print(f"Área de la superficie: {area_superficie:.2f}")
        print(f"Volumen: {volumen:.2f}")
        print(f"Diámetro: {diametro}")

radio = float(input("Introduce el valor del radio de la esfera: "))

esfera = Esfera(radio)
esfera.res()


