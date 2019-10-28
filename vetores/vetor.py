
class Vetor:
    def __init__(self, tamanho):
        self._tamanho = tamanho
        self._elementos = [None] * tamanho
        self._posicao = 0

    def tamanho_vetor(self):
        return len(self._elementos)

    def __str__(self):
        return ' '.join([str(i) for i in self._elementos])

    def contem(self, elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elemento ==  elem:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return i
            return -1

    def inserir_elemento_indice(self, elemento, posicao):
        vetor_inicio =  self._elementos[:posicao] + [None]  # 1, 2, [None]
        vetor_final =  self._elementos[posicao:]            # 3
        vetor_inicio[len(vetor_inicio) - 1] = elemento      # 1, 2, 4, 3
        self._elementos = vetor_inicio + vetor_final        # 1, 2, 4, 3
        self._posicao += 1

    def inserir_elemento_final(self, elemento):
        if self._posicao >= self.tamanho_vetor():
            self._elementos = self._elementos + [None]
            print('posicao_tam: %s é superior ao tamanho atual do vetor: %s! ' % (self._posicao, self._tamanho))
        self._elementos[self._posicao] = elemento
        self._posicao += 1

    def listar_elemento(self, posicao):
        return self._elementos[posicao]

    def remover_elemento_indice(self, posicao):
        vetor_inicio = self._elementos[:posicao] # 1, vetor_inicio
        vetor_final = self._elementos[posicao + 1:] # vetor_final
        self._elementos = vetor_inicio + vetor_final
        self._posicao -= 1

    def remover_elemento(self, elemento):
        posicao = self.indice(elemento)
        self.remover_elemento_indice(posicao)
