import random

from abc import ABC, abstractmethod


class Instrumento(ABC):

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    @abstractmethod
    def serTocado(self):
        pass

    @abstractmethod
    def serAfinado(self):
        pass


class Guitarra(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Cuerda")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Bajo(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Cuerda")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Saxofon(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Viento")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Tambor(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Percusión")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Piano(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Cuerda")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Flauta(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Viento")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Arpa(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Cuerda")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Contrabajo(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Cordofono")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Ukelele(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Cuerda")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Clarinete(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre, "Viento")

    def serTocado(self):
        print(f"{self.nombre} ha sido tocado")

    def serAfinado(self):
        print(f"{self.nombre} ha sido afinado")


class Banda:
    def __init__(self, nombre, musicos):
        self.nombre = nombre
        self.musicos = musicos

    def hacerTocar(self):
        for musico in self.musicos:
            musico.tocar()

    def hacerAfinar(self):
        for musico in self.musicos:
            musico.afinar()


class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def tocar(self):
        print(self.nombre + " va a tocar el/la "+self.instrumento.nombre)
        self.instrumento.serTocado()

    def afinar(self):
        print(self.nombre + " va a afinar el/la " + self.instrumento.nombre)
        self.instrumento.serAfinado()


class Control:
    def __init__(self):
        self.musicos_nombres = ["Juan", "Lauren", "Camila", "Freen",
                                "Daniela", "Rebecca", "Andres", "Milan", "Dinah", "Juliana"]
        self.instrumentos = [
            Guitarra("Guitarra"), Bajo("Bajo"), Saxofon("Saxofón"),
            Tambor("Tambor"), Piano("Piano"), Flauta("Flauta"),
            Arpa("Arpa"), Contrabajo("Contrabajo"), Ukelele(
                "Ukelele"), Clarinete("Clarinete")
        ]

    def crearBanda(self):

        num_integrantes = random.randint(1, 10)

        musicos_seleccionados = random.sample(
            self.musicos_nombres, num_integrantes)

        instrumentos_seleccionados = random.sample(
            self.instrumentos, num_integrantes)

        banda_m_i = [Musico(nombre, instrumento) for nombre, instrumento in zip(
            musicos_seleccionados, instrumentos_seleccionados)]

        nombre_banda = input("Escriba el nombre de la banda: ")
        banda = Banda(nombre_banda, banda_m_i)
        print("\nEl número de musicos en la banda es :", num_integrantes)
        return banda


control = Control()
banda = control.crearBanda()
print("\nTocar instrumentos: ")
banda.hacerTocar()
print("\nAfinación de instrumentos: ")
banda.hacerAfinar()
