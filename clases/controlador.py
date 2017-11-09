import os
from clases.lugar import Lugar

class Controlador(object):

    @classmethod
    def menu(cls):

        print("1: Ver lugares")
        print("2: Crear lugar")
        print("5. Salir")
        print("")
        print("Ingresame que queres hacer")
        ingreso = input()
        return ingreso

    @classmethod
    def menu_creacion(cls):

        print("1: Continente")
        print("2: Pais")
        print("5. Salir")
        print("")
        print("Ingresame que queres crear")
        ingreso = input()
        return ingreso

    @classmethod
    def imprimir_lugar(cls, lista):

        for i in lista:
            print(i.codigo + " | " + i.nombre + " | " + i.tipo + " | " + str(len(i.dependencias)))

    @classmethod
    def crear_lugar(cls, continentes):

        os.system("cls")
        ingreso = Controlador.menu_creacion()
        os.system("cls")
        if ingreso == "1":
            Controlador.ingresar_datos_lugar(continentes, "Continente")
        if ingreso == "2":
            Controlador.ingresar_datos_lugar(continentes, "Pais")
        if ingreso == "5":
            return

    @classmethod
    def ingresar_datos_lugar(cls, continentes, tipo):

        print("Ingresa el codigo")
        #TODO: Verificar que no se repita
        codigo = input()
        print("")

        print("Ingresa el nombre")
        nombre = input()
        print("")

        print("Ingresa las coordenadas")
        x = input()
        y = input()
        print("")

        l = Lugar(codigo, nombre, (x,y), tipo)
        if tipo == "Continente":
            continentes.append(l)
        else:
            Controlador.meter_lista(l, continentes)
        return

    @classmethod
    def meter_lista(cls, lugar, continentes):

        print("Ingrese el codigo de continente")
        continente = input()

        print(lugar.tipo)
        if lugar.tipo != "Pais":
            print("")
            print("Ingrese el codigo de pais")
            pais = input()

        elif lugar.tipo != "Provincia":
            print("")
            print("Ingrese el codigo de provincia")
            provincia = input()

        for con in continentes:
            if str(con.codigo) == continente:
                if lugar.tipo != "Pais":
                    pass
                else:
                    con.dependencias.append(lugar)