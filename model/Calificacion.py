# Calificacion.py
class Calificacion:

    def __init__(self):
        self._nota = None

    def agregar_nota(self):
        
        while True:
            try:
                nota = float(input('Ingrese la nota: '))
                self.validar_nota(nota)
                break
            except ValueError as e:
                print(str(e))

    def validar_nota(self, nota):
        if nota < 1 or nota > 7:
            raise ValueError("Ingreso Invalido: La nota debe ser entre 1 a 7")
        self._nota = nota
    
    def devolver_nota(self):
        if self._nota >= 4:
            return "azul"
        else:
            return "rojo"
        
    @property
    def promedio(self):
        return sum(self.notas) / len(self.notas)
        
    def listado_notas(self):
        return ', '.join(str(nota) for nota in self.notas)
