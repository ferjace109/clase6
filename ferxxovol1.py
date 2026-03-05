from datetime import datetime

class Medicamento:
    def __init__(self, nombre, dosis):
        self.__nombre = nombre
        self.__dosis = dosis 
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis