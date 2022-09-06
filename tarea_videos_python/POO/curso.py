class Curso():
    """
    nombre = "Base de datos"
    creditos = 5
    profesion = "Software"
    """
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"
    
    def mostrarDatos(self):
        dat="Nombre: {0} / Creditos: {1} / Modo de imparticion: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))


