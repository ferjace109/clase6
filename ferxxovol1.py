from datetime import datetime

class Medicamento:
    def __init__(self, nombre, dosis):
        self.__nombre = nombre
        self.__dosis = dosis 
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis
    
if __name__ == "__main__":
    medicamento1 = Medicamento("Paracetamol", 500)
    medicamento2 = Medicamento("Ibuprofeno", 200)
    
    print("Medicamento 1:")
    print("Nombre:", medicamento1.verNombre())
    print("Dosis:", medicamento1.verDosis(), "mg")
    
    print("\nMedicamento 2:")
    print("Nombre:", medicamento2.verNombre())
    print("Dosis:", medicamento2.verDosis(), "mg")