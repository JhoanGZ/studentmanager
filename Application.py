# application.py
from model.Estudiante import Estudiante
from model.Calificacion import Calificacion


class Application:
    
    def main(self):
        while True:
            print('==============================')
            print('1.-Listado de Estudiantes\n2.- Agrega Estudiante\n3.- Ingresar Nota\n4.- Obtener Promedio\n5.- Salir')
            print('==============================')

            app_state = self._get_valid_input('Ingrese una opción: ', [1, 2, 3, 4, 5])
            if app_state == 1:
                Estudiante.show_students()
            elif app_state == 2:
                rut = input('Ingrese el rut del estudiante: ')
                nombre = input('Ingrese el nombre del estudiante: ')
                Estudiante.agregar_estudiante(rut, nombre)
            elif app_state == 3:
                calificacion_instance = Calificacion()
                calificacion_instance.agregar_nota()
            elif app_state == 4:
                calificacion_instance = Calificacion()
                calificacion_instance.validar_nota_entregada()
            elif app_state == 5:
                break
            else:
                print('Opción Invalida')

        print('Terminando el Programa\n¡Gracias por su visita!')
    

    def _get_valid_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            try:
                user_input = int(user_input)
                if user_input in valid_options:
                    return user_input
                else:
                    print('Opción Invalida. Por favor intente de nuevo')
            except ValueError:
                print('Opción de Acceso Invalida. Por favor intente de nuevo')
                
app = Application()
app.main()
