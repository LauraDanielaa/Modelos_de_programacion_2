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
        super().__init__(nombre,"Cuerda")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado")    

class Bajo(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Cuerda")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 
        
class Saxofon(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Cuerda")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 
        
class Tambor(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Percusión")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 
        
class Piano(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Cuerda")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 
        
class Flauta(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Viento")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 
        
class Arpa(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Cuerda")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 
        
class Contrabajo(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Cordofono")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 

class Ukelele(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Cuerda")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 

class Clarinete(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre,"Viento")
    def serTocado(self):
        print("El instrumento ha sido tocado")
    def serAfinado(self):
        print("El instrumento ha sido afinado") 


class Banda:
    def __init__(self,nombre,musicos):
        self.nombre=nombre
        self.musicos=musicos
        
    def hacerTocar(self):
        for musico in self.musicos:
            musico.tocar()
    def hacerAfinar(self):
        for musico in self.musicos:
            musico.afinar()
    
        

class Musico:
    def __init__(self,nombre,instrumento):
        self.nombre=nombre
        self.instrumento=instrumento
    def tocar(self):
        self.instrumento.serTocado()
    def afinar(self):
        self.instrumento.serTocado()
        

class Control:
    def __init__(self, musicos, instrumentos):
        self.musicos=musicos
        self.instrumentos=instrumentos
    def crearBanda():
        banda=Banda()