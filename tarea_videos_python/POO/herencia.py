class Persona():

    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat 
        self.apellidoMaterno = apeMat 
        self.nombre = nom
    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

class Estudiante(Persona):
    def __init__(self,apePat, apeMat, nom, pro):
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro

