class Estudiante:

    def __init__(self, rut='', nombre='', notas=None):
        """
        Initialize the class instance.

        Args:
            rut (str): The rut of the person.
            nombre (str): The name of the person.
            notas (List[float]): The list of grades.

        Raises:
            ValueError: If the rut is not in a valid format, the nombre is empty, or the notas are not valid numbers.
        """
        
        self._rut = rut
        self._nombre = nombre
        if notas is None:
            self._notas = []
        else:
            self._notas = notas

        if not self._is_valid_rut(self._rut):
            raise ValueError("Formato Invalido para el Rut")
        if not self._is_valid_nombre(self._nombre):
            raise ValueError("Nombre no puede quedar en blanco")
        if not self._are_valid_notas(self._notas):
            raise ValueError("Formato invalido de nota")

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
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, notas):
        if not self._are_valid_notas(notas):
            raise ValueError("Formato invalido de nota")
        self._notas = notas

    def add_student(self):
        print('Enter student data: ')
        student = Estudiante()
        rut = self._get_valid_input('Ingresa el Rut del Estudiante ', [])
        for x in self.students:
            if x.rut == rut:
                print('El rut ya se encuentra registrado...')
                return
        student.rut = rut
        name = input('Enter name: ')
        student.name = name
        self.students.append(student)
        


    @property
    def promedio(self):
            return sum(self._notas) / len(self._notas)
        
    def listado_notas(self):
        return ', '.join(str(nota) for nota in self._notas)

    def _is_valid_rut(self, rut):
        # validate rut format
        ...

    def _is_valid_nombre(self, nombre):
        # validate nombre is not empty
        ...

    def _are_valid_notas(self, notas):
        # validate notas are valid numbers
        
        ...
    @classmethod
    def agregar_estudiante(cls, rut, nombre, notas):
        if not cls._is_valid_rut(rut):
            raise ValueError("Formato Invalido para el Rut")
        if not cls._is_valid_nombre(nombre):
            raise ValueError("Nombre no puede quedar en blanco")
        if not cls._are_valid_notas(notas):
            raise ValueError("Formato invalido de nota")
        return cls(rut, nombre, notas)
