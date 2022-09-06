"""Tarea Josue Vallejo"""
import os


os.system("cls")
userJV = input("Ingrese su nombre: ")
os.system("cls")
print(f"Bienvenido {userJV}")

while True:
    try:
        print(" " * 25, "EJERCICIOS")
        print("1. EJERCICIOS DEL 1-10")
        print("2. EJERCICIOS DEL 11-20")
        print("3. EJERCICIOS DEL 21-30")
        print("4. EJERCICIOS DEL 31-39")
        print("Pulse 0 para salir")
        print("*" * 60)
        opcion = int(input("Ingrese la opcion que desea: "))
        if opcion < 0 or opcion > 4:
            os.system("cls")
            print("Ingrese solo numeros entre 0-4.")

        elif opcion == 1:
            os.system("cls")
            print(" " * 25, "Ejercicios 1-10")
            print("1. Hola mundo")
            print("2. Variables")
            print("3. Conversiones")
            print("4. Números y Operaciones")
            print("5. Concatenación")
            print("6. Cadenas")
            print("7. Tuplas")
            print("8. Listas")
            print("9. Diccionarios")
            print("10. Entrada de datos")
            print("*" * 60)
            opcion1 = int(input("Ingrese la opcion que desea: "))
            if opcion1 < 1 or opcion1 > 10:
                os.system("cls")
                print("Solo se aceptan números del 1-10.")
            elif opcion1 == 1:
                os.system("cls")
                print(" " * 20, "EJERCICIO #1")
                print("Hola Mundo")
                print("*" * 60)
            elif opcion1 == 2:
                os.system("cls")
                print(" " * 20, "EJERCICIO #2")
                nombre = "Josue"
                print(nombre)
                print("*" * 50)
                edad = 20
                print(edad)
                edad = True
                print("edad es :", edad)
                print("*" * 50)
                sueldo = 120
                print(sueldo)
                print("*" * 60)
            elif opcion1 == 3:
                os.system("cls")
                print(" " * 20, "EJERCICIO #3")
                numero1 = "35"
                numero2 = "18"
                print(numero1, "+", numero2)
                print("La concatenación es:", numero1 + numero2)
                num1 = int(numero1)
                num2 = int(numero2)
                print("La suma es:", num1 + num2)
                print("*" * 60)
                sueldo = 1200.43
                print("Sueldo:", sueldo)
                sueldoEntero = int(sueldo)
                print("sueldoEntero: ", sueldoEntero)
                print("*" * 60)
                valor = "4500.89"
                valorDecimal = float(valor)
                print("Valor decimal * 3 =", valorDecimal * 3)
                print("*" * 50)
                edad = 100
                print("edad: ", edad)
                print("len de edad es: ", len(str(edad)))
                print("*" * 60)
            elif opcion1 == 4:
                os.system("cls")
                print(" " * 20, "Ejercicio #4")
                entero = 23
                decimales = 31.78
                complejo = 12 + 5j
                booleano = True
                print("entero =", entero)
                print("decimal =", decimales)
                print("complejo =", complejo)
                print("booleano =", booleano)
                num1 = 20
                num2 = 4
                print("Suma:", (num1 + num2))
                print("Resta:", (num1 - num2))
                print("Multiplicación:", (num1 * num2))
                print("División", (num1 / num2))
                print("División Exacta", (num1 // num2))
                print("Potencia:", (num1 ** num2))
                print("*" * 60)
            elif opcion1 == 5:
                os.system("cls")
                print(" " * 20, "EJERCICIO #5")
                texto1 = "Hola"
                texto2 = "Mundo"
                print(texto1, "+", texto2, "=", texto1 + texto2)
                print("El saludo es: %s %s" % (texto1, texto2))
                saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
                print(saludoFinal)
                saludoFinal2 = "Saludo: {y} {x}".format(x=texto1, y=texto2)
                print(saludoFinal2)
                print("*" * 60)
            elif opcion1 == 6:
                os.system("cls")
                print(" " * 20, "EJERCICIO #6")
                texto = "BiEnVeNiDoS al CoDiGo de Josue Vallejo"
                print(texto)
                print(" ")
                print("Todo minusculas:", texto.lower())
                print(" ")
                print("Todo mayusculas:", texto.upper())
                print(" ")
                print("Como titulo::", texto.title())
                print(" ")
                print("En que posicion se encuentra 'al':", texto.find("al"))
                print(" ")
                print("Veces que aparece la letra 'e':", texto.count("e"))
                print(" ")
                textofinal = texto.replace("e", "3")
                print(textofinal)
                print(" ")
                valor = texto.isnumeric()
                print(valor)
                print(" ")
                cadenaseparada = texto.split(" ")
                print(cadenaseparada)
                print(" ")
                print("*" * 60)
            elif opcion1 == 7:
                os.system("cls")
                print(" " * 20, "EJERCICIO #7")
                print("""Una tupla es una estructura de datos de Python, permite almacenar 
distintos valores, son inmutables: no se cambian una vez iniciadas.""")
                print(" ")
                tupla = (1, 2, 3)
                print(tupla)
                print(" ")
                tupla2 = (7, "Josue", True, 450.1, 16 + 7j, "Felicidad", False)
                print(tupla2)
                print(" ")
                tupla3 = (9, 3, (4, 5, 6))
                print(tupla3)
                print(" ")
                print(tupla2[1])
                print(" ")
                # tupla2[1] = "JosueVallejo"
                print(tupla2[-1])  # Accede al último elemento
                print(tupla2[0:4])
                print(tupla2[-2])
                print(" ")
                a, b, c = tupla
                print(a)
                print(b)
                print(c)
                print(" ")
                tuplafinal = tupla + tupla3
                print(tuplafinal)
                print(" ")
                print(tuplafinal.count(2))
                print(tuplafinal.index(3))
                print("*" * 60)
            elif opcion1 == 8:
                os.system("cls")
                print(" " * 20, "EJERCICIO #8")
                print("""Las listas son estructuras de datos que permiten almacenar distintos valores
equivalentes a los arrays en otros lenguajes de programacion, son dinamicas, pueden MUTAR.""")
                lista1 = ["Josue", 25, 98.3, True, "Vallejo", 56.3]
                print(" ")
                print(lista1)
                print(lista1[:])
                print(lista1[2])
                print(lista1[-1])
                print(" ")
                print(lista1[0:3])
                print(lista1[:2])
                print(lista1[3:])
                print(" ")
                lista1.append("SVALLEJOS22")
                print(lista1)
                print(" ")
                lista1.insert(4, "Ecuador")
                print(lista1)
                print(" ")
                lista1.extend(["Alejandro", 110, False])
                print(lista1)
                print(" ")
                print(lista1.index("Vallejo"))
                print(" ")
                lista1.remove(56.3)
                print(lista1)
                print(" ")
                lista1.pop
                print(lista1)
                print(" ")
                lista2 = ["Milagro", "Guayaquil"]
                lista3 = lista1 + lista2
                print(lista3)
                print(" ")
                print(lista2 * 4)
                print(" ")
                print("SVALLEJOS" in lista1)
                print("*" * 60)
            elif opcion1 == 9:
                os.system("cls")
                print(" " * 20, "EJERCICIO #9")
                miDiccionario = {"España": "Madrid", "Ecuador": "Milagro", "Alemania": "Berlín"}
                print(" ")
                print(miDiccionario["Ecuador"])
                print(miDiccionario)
                print(" ")
                miDiccionario["Venezuela"] = "Caracas"
                print(miDiccionario)
                print(" ")
                miDiccionario["España"] = "Barcelona"
                print(miDiccionario)
                print(" ")
                del miDiccionario["España"]
                print(miDiccionario)
                print(" ")
                dic2 = {"Vallejo": "Josue", 20: True, "Sueldo": 220.08}
                print(dic2[20])
                print(" ")
                llaves = ("España", "Francia", "Inglaterra")
                dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
                print(dicPaises)
                print(" ")
                datosPersonales = {"Apellido": "Vallejo", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
                print(datosPersonales)
                print(datosPersonales["Anios"])
                print(" ")
                print(datosPersonales.get('Ape', "Josue"))
                print(" ")
                print(datosPersonales.keys())
                valores = tuple(datosPersonales.values())
                print(valores)
                print("*" * 60)
            else:
                os.system("cls")
                print(" " * 20, "EJERCICIO #10")
                nombre = input("Ingrese su nombre: ")
                edad = int(input("Ingrese su edad: "))
                sueldo = float(input("Ingrese su sueldo: "))
                print(f"Hola {nombre}")
                print(f"Tu edad es: {edad}")
                edadfutura = edad + 20
                print(f"Tu edad dentro de 20 años, sera: {edadfutura}")
                print(f"Su sueldo es: {sueldo}")
                print("*" * 60)

        elif opcion == 2:
            os.system("cls")
            print(" " * 25, "Ejercicios 11-20")
            print("11. If-Else")
            print("12. Funciones")
            print("13. Operadores Logicos")
            print("14. Operador Ternario")
            print("15. Funcion Range")
            print("16. Bucle FOR")
            print("17. If con tuplas")
            print("18. Factorial de un número")
            print("19. Bucle While")
            print("20. Sentencias Break, Continue y Pass")
            print("*" * 60)
            opcion2 = int(input("Ingrese la opcion que desea: "))
            if opcion2 < 11 or opcion2 > 20:
                os.system("cls")
                print("Solo se aceptan numeros del 11-20")
            elif opcion2 == 11:
                os.system("cls")
                print(" " * 20, "EJERCICIO #11")
                edadjosue = int(input("Ingrese su edad: "))
                if edadjosue > 18:
                    print("Eres mayor de edad!!")
                elif edadjosue == 18:
                    print("Tienes 18 años.")
                else:
                    print("No eres mayor de edad.")
                print("*" * 60)
            elif opcion2 == 12:
                os.system("cls")
                print(" " * 20, "EJERCICIO #12")
                print("""Una Función es un conjunto de instrucciones que realiza un proceso o tarea
su principal ventaja es que ayudan a evitar codigo repetido.""")


                def saludarjv():
                    print("Vallejo")
                    print("Josue")
                    print("svallejos22")
                    return "Hola"


                print(saludarjv())
                print(" ")


                def evaluarSueldoMinimo(sueldo):
                    if sueldo >= 425:
                        print("Cumples con el sueldo")
                    else:
                        print("Ganas menos que el sueldo mínimo")


                evaluarSueldoMinimo(750)
                print("*" * 60)
            elif opcion2 == 13:
                os.system("cls")
                print(" " * 20, "EJERCICIO #13")
                print("""AND: Y si ademas...
OR: O sino
not: negación""")
                print(" ")
                distancia = 300
                numeroHermanos = 3
                salarioPadres = 3000
                tieneBeneficio = False
                if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
                    tieneBeneficio = True
                print("tiene beneficio: ", not tieneBeneficio)
                print(" ")
                if (5 > 3) or (8 < 6):
                    print("Verdad")
                else:
                    print("Es mentira")
                print("*" * 60)
            elif opcion2 == 14:
                os.system("cls")
                print(" " * 20, "EJERCICIO #14")
                """
                String sexo;
                sexo = (10 > 20) ? "Masculino" : "Femenino";
                """

                sexosJV = ("Hombre", "Mujer")

                posicion = True
                JVsexo = sexosJV[posicion]  # Mujer
                print(JVsexo)
                JVsexo = sexosJV[not posicion]  # Hombre
                print(JVsexo)
                print("*" * 60)
            elif opcion2 == 15:
                os.system("cls")
                print(" " * 20, "EJERCICIO #15")
                numeros = range(5)  # [0, 1, 2, 3, 4]
                print(numeros[1])

                numeros1 = range(4, 10)  # [4,5,6,7,8,9]
                print(numeros1[5])

                numeros2 = range(10, 100, 8)
                print(numeros2[9])
                print("*" * 60)
            elif opcion2 == 16:
                os.system("cls")
                print(" " * 20, "EJERCICIO #16")
                for i in range(1, 13):
                    print("{0} x {1} es: {2}".format(i, i, (i * i)))
                for nom in ["josue", "vallejo", "suarez"]:
                    print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
                print("*" * 60)
            elif opcion2 == 17:
                os.system("cls")
                print(" " * 20, "EJERCICIO #17")
                print("--Cursos--")
                print("Matemáticas - Biologia - Lenguaje - Ciencias")
                curso = input("Ingrese el curso que desea: ")
                if curso in ("Matemáticas", "Biologia", "Lenguaje", "Ciencias"):
                    print("Curso {0} seleccionado.".format(curso))
                else:
                    print("No existe el curso.")
                print("*" * 60)
            elif opcion2 == 18:
                os.system("cls")
                print(" " * 20, "EJERCICIO #18")
                # Factorial: Es el producto de todos los números positivos enteros comprendidos entre 1 y un número.

                # Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
                # Factorial de 4: 1 * 2 * 3 * 4 = 24

                numero = int(input("Ingrese un número: "))

                jvfactorial = 1
                for n in range(1, (numero + 1)):
                    factorial = jvfactorial * n

                print("El factorial de {0} es: {1}".format(numero, jvfactorial))

                print("*" * 60)
            elif opcion2 == 19:
                os.system("cls")
                print(" " * 20, "EJERCICIO #19")
                # While es una estructura repetitiva que nos permire realizar multiples
                # iteraciones basadas en el resultado de una expresion logica que puede tener
                # como resultado un valor True o False
                indice = 1
                while indice <= 10:
                    print("Valor actual: {0}".format(indice))
                    indice = indice + 1
                print("Hemos terminado el bucle while.")
                print("*" * 60)
                inicio = 2
                while inicio <= 100:
                    print("Numero par: {0}".format(inicio))
                    inicio += 2
                print("Hemos terminado el bucle while.")
                print("*" * 60)
            else:
                os.system("cls")
                print(" " * 20, "EJERCICIO #20")
                for numero in range(1, 6):
                    if numero == 3:
                        continue
                    print("El numero es: {0}".format(numero))
                print("Bucle terminado.")
                # Pass: Permite continuar con una sentencia o función que ya no tiene
                # o aún no tiene un bloque de código útil.
                for numero2 in range(1, 6):
                    if numero2 <= 3:
                        # aquí no pasa nada y el bucle sigue trabajando.
                        pass
                    else:
                        print("El siguiente valor es mayor a 3:")
                    print("El número es: {0}".format(numero2))
                print("Bucle terminado.")


                def funcionSinImplementar():
                    pass


                print("*" * 60)

        elif opcion == 3:
            os.system("cls")
            print(" " * 25, "Ejercicios 21-30")
            print("21. Generadores en python (yield)")
            print("22. Generadores en python (yield from)")
            print("23. Excepciones en python")
            print("24. Sentencia Raise")
            print("25. Modulos en python")
            print("26. Paquetes en python")
            print("27. POO")
            print("28. Constructores")
            print("29. Encapsulamiento de variables")
            print("30. Encapsulamiento de metodos")
            print("*" * 60)
            opcion3 = int(input("Ingrese la opción que desea: "))
            if opcion3 < 21 or opcion3 > 30:
                os.system("cls")
                print("Solo se aceptan numeros del 21-30")
            elif opcion3 == 21:
                os.system("cls")
                print(" " * 20, "EJERCICIO #21")
                """
                def generaMultiplos7(limite):
                    numero = 1
                    listaNumeros = []

                    while numero <= limite:
                        listaNumeros.append(numero * 7)
                        numero = numero + 1
                    return listaNumeros  # Retorna toda la lista creada.

                print(generaMultiplos7(10))
                """
                def generadorMultiplos7(limite):
                    numero = 1

                    while numero <= limite:
                        yield numero * 7  # ceder. la instrucción "yield" genera un objeto iterable
                        numero = numero + 1
                obtieneMultiplos7 = generadorMultiplos7(10)
                """
                # print(obtieneMultiplos7)
                for n in obtieneMultiplos7:
                    print(n)
                """
                # next(): Retorna el siguiente elemento de un objeto iterable:
                print(next(obtieneMultiplos7))
                print("Acá hay 300 líneas de código...")
                print(next(obtieneMultiplos7))
                print("Acá hay 1000 líneas de código...")
                print(next(obtieneMultiplos7))
                # Son más eficiente que las funciones tradicionales.
                # Muy útiles con listas de valores infinitos.
                # Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).
                print("*" * 60)
            elif opcion3 == 22:
                os.system("cls")
                print(" " * 20, "EJERCICIO #22")
                """
                def devuelveLenguajes(*lenguajes):
                    for leng in lenguajes:
                        yield leng
                """
                def devuelveLenguajes(*lenguajes):
                    for leng in lenguajes:
                        yield from leng
                lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
                print(next(lenguajesObtenidos))
                print(next(lenguajesObtenidos))
                print("*" * 60)
            elif opcion3 == 23:
                os.system("cls")
                print(" " * 20, "EJERCICIO #23")
                "Excepción: Error en tiempo de ejecución (durante la ejecución de un programa)."
                numero1 = 20
                numero2 = 2
                """print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))"""
                try:
                    resultado = numero1 / numero2
                # except:
                except ZeroDivisionError:
                    print("No se puede dividir entre 0...")
                finally:
                    print("Yo siempre aparezco")
                print("Aquí culmina mi programa")
                print("*" * 60)
            elif opcion3 == 24:
                os.system("cls")
                print(" " * 20, "EJERCICIO #24")
                # Raise: Sirve para lanzar (de forma intencional) excepciones en Python.
                def evaluarNota(nota):
                    if nota < 0:
                        raise ValueError("Valor incorrecto...")
                        # raise ZeroDivisionError("Este mensaje es personalizado.")
                    elif nota >= 16:
                        print("Excelente")
                    elif nota >= 11:
                        print("Aprobado")
                    else:
                        print("Desaprobado")
                evaluarNota(-7)
                print("Este es el fin de mi programa.")
                print("*" * 60)
            elif opcion3 == 25:
                os.system("cls")
                print(" " * 20, "EJERCICIO #25")
                from modulos.funcionesMatematicas import sumar, multiplicar
                print("La suma es: ", sumar(5, 6))
                print("La multiplicación es: ", multiplicar(5, 6))
                print("*" * 60)
            elif opcion3 == 26:
                os.system("cls")
                print(" " * 20, "EJERCICIO #26")
                """
                   Paquetes:
                   Directorios (carpetas) donde se almacenan módulos relacionados entre sí.

                   ¿Para qué sirven?
                   Para organizar mejor el código y poder reutilizarlo mejor (modularización y reutilización).

                   ¿Cómo se crea un paquete?
                   Crear una carpeta o directorio con un archivo dentro llamado __init__.py

                   Lo que hace __init__.py es "convertir" un directorio en un módulo (paquete)
                   que contiene otros módulos, y esto lo hace para poder importarlos.
                   """
                from Paquete1.funcionesCadenas import contarLetras
                from Paquete1.funcionesNumericas import *
                print("El len de 'JosueVallejo22082002' es: ", contarLetras("JosueVallejo22082002"))
                print("La multiplicación 5*8 es: ", multiplicar(5, 8))
                print("La potenciación 2**5 es: ", potenciar(2, 5))
                print("*" * 60)
            elif opcion3 == 27:
                from POO.persona import Persona
                os.system("cls")
                print(" " * 20, "EJERCICIO #27")
                persona1 = Persona()
                persona1.apellidos = "Vallejo Suarez"
                persona1.nombres = "Josue"
                print(persona1.apellidos, persona1.nombres)
                persona1.despertar()
                print(persona1.despierta)
                persona2 = Persona()
                persona2.apellidos = "Paz Torres"
                persona2.nombres = "David"
                print(persona2.apellidos, persona2.nombres)
                #persona1.despertar
                print(persona2.despierta)
                print("*" * 60)
            elif opcion3 == 28:
                from POO.curso import Curso
                os.system("cls")
                print(" " * 20, "EJERCICIO #28")
                curso1 = Curso("Base de datos", 5, "Software")
                print(curso1.nombre)
                curso2 = Curso("Estructura de datos", 5, "Software")
                print(curso2.nombre)
                print("*" * 60)
            elif opcion3 == 29:
                os.system("cls")
                print(" " * 20, "EJERCICIO #29")
                from POO.curso import Curso
                curso1 = Curso("Matematicas",5,"Software")
                print(curso1.nombre)
                curso1.imparticion = "Virtual"
                print(curso1.imparticion)
                curso1.mostrarDatos()
                print("*" * 60)
            else:
                from POO.curso2 import Curso
                os.system("cls")
                print(" " * 20, "EJERCICIO #30")
                curso1 = Curso("BDD",5,"Software")
                print(curso1.nombre)
                curso1.mostrarDatos()
                print("*" * 60)
        elif opcion == 4:
            os.system("cls")
            print(" " * 25, "Ejercicios 31-38")
            print("31. Metodos Accesores")
            print("32. Metodos de clase _str_")
            print("33. Herencia en python")
            print("34. Sobreescritura de métodos")
            print("35. Principios de sustitución entre Clases")
            print("36. Herencia MÚLTIPLE")
            print("37. Polimorfismo")
            print("38. Relaciones entre clases")
            print("39. FINAL DE LA TAREA")
            print("*" * 60)
            opcion4 = int(input("Ingrese la opcion que desea: "))
            if opcion4 < 31 or opcion4 > 39:
                os.system("cls")
                print("Solo se aceptan números del 31-39")
            elif opcion4 == 31:
                from POO.cuenta import Cuenta
                os.system("cls")
                print(" " * 20, "EJERCICIO #31")
                cuenta1 = Cuenta("Josue Vallejo", 650, "Dolares")
                print(cuenta1.get_saldo())
                print(cuenta1.get_Moneda())
                cuenta1.set_moneda("Euros")
                print(cuenta1.get_Moneda())
                print("*" * 60)
            elif opcion4 == 32:
                from POO.curso3 import *
                os.system("cls")
                print(" " * 20, "EJERCICIO #32")
                curso1 = Curso("BDD",5,"Software")
                print(curso1)
                curso1.mostrarDatos()
                print("*" * 60)
            elif opcion4 == 33:
                from POO.herencia import *
                os.system("cls")
                print(" " * 20, "EJERCICIO #33")
                estudiante1 = Estudiante("Vallejo", "Suarez", "Josue", "Software")
                print(estudiante1.mostrarNombreCompleto())
                print(estudiante1.profesion)
                print("*" * 60)
            elif opcion4 == 34:
                from POO.herencia2 import *
                os.system("cls")
                print(" " * 20, "EJERCICIO #34")
                estudiante1 = Estudiante("Vallejo", "Suarez", "Josue", "Software")
                estudiante1.datos()
                print("*" * 60)
            elif opcion4 == 35:
                from POO.herencia2 import *
                os.system("cls")
                print(" " * 20, "EJERCICIO #35")
                estudiante1 = Estudiante("Vallejo", "Suarez", "Josue", "Software")
                persona1 = Persona("Vallejo", "Suarez", "Josue")
                print(isinstance(estudiante1, Estudiante))
                print(isinstance(estudiante1, Persona))
                print(isinstance(persona1, Persona))
                print(isinstance(persona1, Estudiante))
                print("*" * 60)
            elif opcion4 == 36:
                from POO.HerenciaMultiple import  *
                os.system("cls")
                print(" " * 20, "EJERCICIO #36")
                cx1 = ClaseX(22, 19)
                print(cx1.parametro1, cx1.parametro2)
                print("*" * 60)
            elif opcion4 == 37:
                from POO.Polimorfismo import *
                os.system("cls")
                print(" " * 20, "EJERCICIO #37")
                docente1 = Trabajador()
                describirPersona(docente1)
                print("*" * 60)
            elif opcion4 == 38:
                from POO.relacionesclases import *
                os.system("cls")
                print(" " * 20, "EJERCICIO #38")
                pais1 = Pais("Ecuador", "Guillermo Lasso")
                print(pais1)
                ciudad1 = Ciudad("Milagro", 100000, pais1)
                print(ciudad1)
                ciudadela1 = Ciudadela("17 Septiembre", ciudad1)
                print(ciudadela1)
                print("*" * 60)
            else:
                os.system("cls")
                print(" " * 20, "FINAL")
                print("""ESTE ES EL FINAL DE MI TAREA CON RESPECTO A LA REVISION, 
LECTURA Y SEGUIMIENTO DE LOS 40 VIDEOS DEL CURSO DE PYTHON.
ESTUDIANTE: JOSUE VALLEJO
CARRERA: SOFTWARE - 4TO SEMESTRE.""")
                print("*" * 60)
                break
        else:
            os.system("cls")
            print(f"Gracias por su visita {userJV}!!!")
            break
    except ValueError:
        os.system("cls")
        print("No se admiten letras, solo números. Ingrese nuevamente.")
