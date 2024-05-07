class Persona:

    def __init__(self, nombre: str = "john", apellido: str = "doe", du: int = 123456):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du

    def mostrar_datos(self):
        print(f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}')

if __name__ == '__main__':
    persona = Persona () 
    print (persona)
    print (persona.__str__())

    persona = Persona ()
    print (persona)          

    persona = Persona ()
    print (persona)    