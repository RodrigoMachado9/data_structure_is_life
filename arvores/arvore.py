

class Arvore:

    def __init__(self, raiz=None):
        self.__raiz = raiz


    @property
    def raiz(self):
        return self.__raiz

    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if (self.__raiz == None):
            self.__raiz = no
        else:
            if (self.__raiz.peso()  > no.peso()):
                self.__raiz.no_esquerdo = no
            self.__raiz.no_direito = no

    def __inserir(self, referencia, novo_no):
        if referencia.peso() < novo_no.peso():
            if referencia.no_direito == None:
                referencia.no_direito = novo_no
            else:
                self.__inserir(referencia.no_direito, novo_no)
        else:
            if referencia.no_esquerdo == None:
                referencia.no_esquerdo =  novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)


