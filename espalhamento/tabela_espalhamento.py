from listas.lista_ligada import ListaLigada


class TabelaEspalhamento:

    def __init__(self):
        self.__elementos = ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0


        for i in range(self.__numero_categorias):
            self.__elementos.inserir(ListaLigada())

    def __gerar_espalhamento(self, elemento):
        return hash(elemento) % self.__numero_categorias

    def inserir(self, elemento):
        if self.contem(elemento):
            return False
        numero_espalhamento =  self.__gerar_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.remover(elemento)
        self.__tamanho -= 1

    def remover(self, elemento):
        numero_espalhamento = self.__gerar_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.inserir(elemento)
        self.__tamanho += 1
        return True

    def contem(self, elemento):
        numero_espalhamento = self.__gerar_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        return categoria.contem(elemento)

    def __str__(self):
        return self.__elementos.__str__()