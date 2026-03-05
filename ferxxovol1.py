from datetime import datetime

class Medicamento:
    def __init__(self, nombre, dosis):
        self.__nombre = nombre
        self.__dosis = dosis 
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis
    
class Mascota:
    def __init__(self, nombre, historia, tipo, peso, fecha_ingreso):
        self.__nombre = nombre
        self.__historia = historia
        self.__tipo = tipo
        self.__peso = peso
        self.__fecha_ingreso = fecha_ingreso
        self.__lista_medicamentos = []
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarLista_Medicamentos(self, medicamentos):
        self.__lista_medicamentos = medicamentos
    
if __name__ == "__main__":
    medicamento1 = Medicamento("Paracetamol", 500)
    medicamento2 = Medicamento("Ibuprofeno", 200)
    
    mascota1 = Mascota("Firulais", 123, "Perro", 20.5, datetime(2023, 5, 1))
    mascota1.asignarLista_Medicamentos([medicamento1, medicamento2])
    
    print("Nombre de la mascota:", mascota1.verNombre())
    print("Historia clínica:", mascota1.verHistoria())
    print("Tipo de mascota:", mascota1.verTipo())
    print("Peso de la mascota:", mascota1.verPeso(), "kg")
    print("Fecha de ingreso:", mascota1.verFecha().strftime("%Y-%m-%d"))
    
    print("\nMedicamentos asignados:")
    for med in mascota1.verLista_Medicamentos():
        print("- Nombre:", med.verNombre(), ", Dosis:", med.verDosis(), "mg")