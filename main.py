from vetores.vetor import Vetor
from listas.lista_ligada import ListaLigada
from listas_duplamente_ligada.lista_duplamente_ligada import ListaLigada as ListaDuplamenteLigada
from pilhas.pilha import Pilha
from filas.fila import Fila
from conjuntos.conjunto import Conjunto
from mapas.mapa import Mapa


print(30 * '-', 'MENU', 30 * '-')
print('1. vetores')
print('2. listas ligadas')
print('3. listas duplamente ligadas')
print('4. pilhas')
print('5. filas')
print('6. conjuntos')
print('7. mapas')

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

elif menu == 4:
    pilha_teste = Pilha()
    print(pilha_teste.empilhar(3))
    print(pilha_teste.empilhar(5))
    print(pilha_teste.empilhar(7))
    print(pilha_teste.desempilhar())
    print(pilha_teste.desempilhar())

elif menu == 5:
    fila_teste = Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    fila_teste.enfileirar(4)
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)

elif menu == 6:
    conjunto_teste = Conjunto()
    conjunto_teste.inserir(2)
    conjunto_teste.inserir(3)
    conjunto_teste.inserir(4)
    # conjunto_teste.inserir_posicao(0, 5)
    print(conjunto_teste)

elif menu == 7:
    mapa_teste = Mapa()
    mapa_teste.adicionar("par", 10)
    mapa_teste.adicionar("impar", 5)
    mapa_teste.adicionar("par", 2)
    print(mapa_teste)
    print(mapa_teste.contem_chave("par"))
    print(mapa_teste.recuperar("par"))

else:
    print('Opção inválida')