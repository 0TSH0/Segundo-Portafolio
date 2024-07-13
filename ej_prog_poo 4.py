# 4.- Diseñe una clase que represente a una pizza con su nombre, listado de ingredientes, tamaño, precio de venta, costo de producción y tiempo de producción, y que permita determinar la ganancia neta y comprobar si contiene un ingrediente específico. 
# Entrada: 	Nombre: Vegetariana 
#  	 	Ingredientes: [“Ají”, “Cebolla”, “Tomate”, “Champiñón”] 
#  	 	Tamaño: Mediano 
#  	 	Precio de venta: RD$725 
#  	 	Costo de producción: RD$450 
 	 
#  	Tiempo de cocción: 7 minutos 
# Salida: 	Ganancia neta: RD$275 
#  	 	¿Contiene “Ají”?: Verdadero 

class Pizza:
    def __init__(self, nombre, ingredientes, tamano, precio_venta, costo_produccion, tiempo_coccion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.tamano = tamano
        self.precio_venta = precio_venta
        self.costo_produccion = costo_produccion
        self.tiempo_coccion = tiempo_coccion

    def ganancia_neta(self):
        return self.precio_venta - self.costo_produccion

    def ingredientes(self, ingrediente):
        return ingrediente in self.ingredientes

    def res(self):
        ganancia_neta = self.ganancia_neta()
        print(f"Nombre: {self.nombre}")
        print(f"Ingredientes: {', '.join(self.ingredientes)}")
        print(f"Tamaño: {self.tamano}")
        print(f"Precio de venta: RD${self.precio_venta}")
        print(f"Costo de producción: RD${self.costo_produccion}")
        print(f"Tiempo de cocción: {self.tiempo_coccion} minutos")
        print(f"Ganancia neta: RD${ganancia_neta:.2f}")

nombre = input("Introduce el nombre de la pizza: ")
ingredientes = input("Introduce los ingredientes de la pizza, separados por comas: ").split(',')
ingredientes = [ingrediente.strip() for ingrediente in ingredientes]
tamano = input("Introduce el tamaño de la pizza: ")
precio_venta = float(input("Introduce el precio de venta de la pizza (RD$): "))
costo_produccion = float(input("Introduce el costo de producción de la pizza (RD$): "))
tiempo_coccion = int(input("Introduce el tiempo de cocción de la pizza (minutos): "))

pizza = Pizza(nombre, ingredientes, tamano, precio_venta, costo_produccion, tiempo_coccion)
pizza.res()

ingrediente_buscado = input("Introduce un ingrediente para verificar si la pizza lo contiene: ")
contiene = pizza.ingredientes(ingrediente_buscado)
print(f"La pizza {'sí' if contiene else 'no'} contiene {ingrediente_buscado}.")

