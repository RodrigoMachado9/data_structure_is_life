from vetores.vetor import Vetor
from listas.lista_ligada import ListaLigada
from listas.duplamente_ligada.lista_duplamente_ligada import ListaLigada as ListaDuplamenteLigada

print(30 * '-', 'MENU', 30 * '-')
print('1. vetores')
print('2. listas ligadas')
print('3. listas duplamente ligadas')

menu = int(input('Digite a opção desejada: '))

if menu == 1:
    vetor_teste = Vetor(0)
    vetor_teste.inserir_elemento_indice(1, 0)
    vetor_teste.inserir_elemento_indice(2, 1)
    vetor_teste.inserir_elemento_indice(3, 2)
    vetor_teste.inserir_elemento_indice(4, 2)

    """
    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))
    print(vetor_teste.listar_elemento(2))
    """
    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))
    print(vetor_teste.listar_elemento(2))
    print(vetor_teste.listar_elemento(3))
    print(vetor_teste.indice(3))
    print(vetor_teste.indice(9))

elif menu == 2:
    lista_teste  = ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 22)
    print(lista_teste)
    print(lista_teste.contem(5))
    print(lista_teste.indice(5))

elif menu == 3:
    lista_teste  = ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 22)
    print(lista_teste)
    print(lista_teste.contem(5))
    print(lista_teste.indice(5))