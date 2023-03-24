from dataclasses import dataclass
from typing import List


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        name_1 = self.nombre
        name_2 = other.nombre
        if name_1 == name_2:
            return True
        else:
            return False

class Conjunto:
    contador = 0


    def __init__(self, nombre, Contador):
        self.name: list[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property    #Así se define una propiedad de sólo lectura
    def __id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return any(e.nombre == elemento.nombre for e in self.elementos)

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for e in otro_conjunto.elementos:
            if not self.contiene(e):
                self.elementos.append(e)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(self.nombre + " UNIDO " + otro_conjunto.nombre)
        nuevo_conjunto.elementos = self.elementos.copy()
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [e for e in conjunto1.elementos if conjunto2.contiene(e)]
        nuevo_conjunto = Conjunto(conjunto1.nombre + " INTERSECTADO " + conjunto2.nombre)
        nuevo_conjunto.elementos = elementos_comunes
        return nuevo_conjunto

    def __str__(self):
        nombres_elementos = ", ".join(e.nombre for e in self.elementos)
        return f"Conjunto {self.nombre}: ({nombres_elementos})"