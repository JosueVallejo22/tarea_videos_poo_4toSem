# Polimorfismo viene de 2 palabras (poli -> muchas/ morfos -> formas)

class Estudiante():

    def describir(self):
        print("Josue Vallejo es buen estudiante.")


class Docente():
    def describir(self):
        print("Me dedico a enseñar cursos")


class Trabajador():
    def describir(self):
        print("Trabajo dentro de una gran empresa")


def describirPersona(persona):
    persona.describir()
