from abc import ABC, abstractclassmethod

class NoArvore(ABC):
    def __init__(self, valor, no_esquerdo=None, no_direito=None):
        self._valor = valor     # atributo protegido
        self.__no_esquerdo = no_esquerdo
        self.__no_direito = no_direito

    @property
    def valor(self):
        return self._valor

    @property
    def no_esquerdo(self):
        return self.__no_esquerdo

    @property
    def no_direito(self):
        return self.__no_direito

    @no_direito.setter
    def no_direito(self, no_direito):
        self.__no_direito = no_direito

    @no_esquerdo.setter
    def no_esquerdo(self, no_esquerdo):
        self.__no_esquerdo = no_esquerdo

    @abstractclassmethod
    def peso(self):
        pass

    def __str__(self):
        return ("[(X)]" if self.__no_esquerdo == None else f"[({self.__no_esquerdo.__str__()})]") + \
                 (f"[({self.valor.__str__()})]") + \
                    ("[(X)]" if self.__no_direito == None else f"[({self.__no_direito.__str__()})]")
