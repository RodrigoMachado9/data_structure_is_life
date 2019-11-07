# no_arvore_cliente, no_arvore_pessoa, no_arvore_float .... etc
from arvores.no_arvore import NoArvore
class NoArvoreInteiro(NoArvore):

    def __init__(self, valor):
        super(NoArvoreInteiro, self).__init__(valor)


    def peso(self):
        return self.valor
