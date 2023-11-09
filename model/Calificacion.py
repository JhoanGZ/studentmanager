
class Calificacion:

    def __init__(self, nota):
        """
        Initializes a new instance of the Calificacion class.
        Args:
            nota (float): The nota value for the Calificacion object.
        Raises:
            ValueError: If the nota is below 1 or above 7, or if it is not a valid number.
        """
        self.agregar_nota(nota)
        self._nota = nota
        
    

    def agregar_nota(self, nota):
        """
        Validates the nota input.
        Args:
            nota (float): The nota value to be validated.
        Raises:
            ValueError: If the nota is below 1 or above 7, or if it is not a valid number.
        """
        if not isinstance(nota, (int, float)):
            raise ValueError(f'Invalid input: [{nota}]. Please enter a valid number.')
        if nota < 1:
            raise ValueError(f'The entered grade [{nota}] is below one! It cannot be entered.')
        if nota >= 7:
            raise ValueError(f'The entered grade [{nota}] is above seven! It cannot be entered.')

    def validar_nota_entregada(self, nota):
        """
        Validates nota and returns as indicated.
        Args:
            nota (float): Note must be valid.
        Returns:
            float: Insert the new value if it's instructed.
        Raises:
            ValueError: If the value is below 1 or above 7.
        """
        self._nota = float(nota)
        if self._nota <= 7 and self._nota >= 1:
            pass
        else:
            raise ValueError("Ingreso Invalido: La nota debe ser entre 1 a 7")
    
    def devolver_nota(self):
        if self._nota >= 4:
            return "azul"
        else:
            return "rojo"