from model.Calificacion import Calificacion

class Estudiante:

    _estudiantes = []

    def __init__(self, rut='', nombre='',  notas= None):
        self._rut = rut
        self._nombre = nombre

    @property
    def rut(self):
        return self._rut

    @rut.setter
    def rut(self, rut):
        if not self._is_valid_rut(rut):
            raise ValueError("Formato Invalido para el Rut")
        self._rut = rut

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not self._is_valid_nombre(nombre):
            raise ValueError("Nombre no puede quedar en blanco")
        self._nombre = nombre

    @property
    def _is_valid_rut(self, rut):
        return bool(rut)
        
    def _is_valid_nombre(self, nombre):
        return bool(nombre)
        
        
    @classmethod
    def agregar_estudiante(cls, rut, nombre, notas=None):
            
            student = cls(rut, nombre)
            cls._estudiantes.append(student)
            
    @classmethod
    def show_students(cls):
        if not cls._estudiantes:
            print('No hay estudiantes registrados')
        else:
            for i in cls._estudiantes:
                print(f'Nombre estudiante: {i.nombre}, Rut: {i.rut}')
