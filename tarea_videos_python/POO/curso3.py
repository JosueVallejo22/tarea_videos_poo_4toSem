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
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado")
        else:
            print("No es necesario asignar docente.")
    def __verificarDocente(self):
        print("Verificando si existe docente asignado.")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
    def __str__(self):
        texto = "Nombre : {0} - Creditos: {1}"
        return texto.format(self.nombre, self.creditos)


