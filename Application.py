from model.Estudiante import Estudiante
from model.Calificacion import Calificacion
from symbol import classdef

class Application:
    
    def main(self):
         while True:
            print('==============================')
            print('1.-Listado de Estudiantes\n2.- Agrega Estudiante\n3.- Ingresar Nota\n4.- Obtener Promedio\n5.- Salir')

            app_state = self._get_valid_input('Ingrese una opción: ', [1, 2, 3, 4, 5])
            if app_state == 1:
                Estudiante.listado_notas()
            elif app_state == 2:
                Estudiante.add_student()
            elif app_state == 3:
                Calificacion.agregar_nota()
            elif app_state == 4:
                Calificacion.validar_nota_entregada(self)
            elif app_state == 5:
                print('Terminando el Programa...\n¡Gracias por su visita!')
                break
            else:
                print('Invalid option')

            print('Terminando el Programa...\n¡Gracias por su visita!')
    

    @classdef
    def _get_valid_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            try:
                user_input = int(user_input)
                if user_input in valid_options:
                    return user_input
                else:
                    print('Invalid option. Please try again.')
            except ValueError:
                print('Invalid access option. Please try again.')
                
app = Application()
app.main()

