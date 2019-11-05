from listas.lista_ligada import ListaLigada
from mapas.associacao import Associacao
# 0: ("par":10)

class Mapa:

    def __init__(self):
        self.__elementos = ListaLigada()
        self.__numero_categorias = 10

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(ListaLigada())


    def gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__numero_categorias


    def contem_chave(self, chave):
        numero_espalhamento = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:
                return True
        return False


