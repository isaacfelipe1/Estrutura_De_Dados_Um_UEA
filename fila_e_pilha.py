'''Um programa utilizando Fila e Pilha'''
""" O programa insere, remove, busca elemento  e imprime, de acordo com a Fila e Pilha. 
Definição:  Na fila o primeiro que entra é o primeiro a sair, na pilha o primeiro a entrar é o último a sair!""" 
#@autor Isaac Felipe! 
from time import sleep
from typing import Deque, Any
from collections import deque
from typing import List
'''Bem vindo ao Programa!'''
print("\tBem vindo ao programa! :)\n")
sleep(2)
print("="*35)
print("\nEscolha uma opção\n")#Escolha uma opção
option=0
cont=0
d=None
while option!=3:
    print('''        [1]-Fila
        [2]-Pilha
        [3]-Sair do programa
    ''')
    '''Escolha sua opção ou digite 3 para sair!'''
    option=int(input("Escolha uma opção ou digite (3) para sair\n"))
    # um condição de erro, se for maior que 3 ou se for igual a 0, irá mostrar essa mensagem personalizada de erro.
    while option >3 or option==0: 
        '''Errro! Digite de acordo com a númeração!'''
        print("\nErro! Digite de acordo com a númeração\n")
        print('''        [1]-Fila
        [2]-Pilha
        [3]-Sair do programa
    
        ''')
        '''Escolha sua opção ou digite 3 para sair!'''
        option=int(input("Escolha uma opção ou digite (3)- para sair\n"))
    if option==3:
        print("Finalizando")
        sleep(2)
        print('\nSaiu! Volte sempre :)\n')
    if option==1:
        print('\tBem-vindo ao programa\n ')
        sleep(2)
        option=0
        queue:Deque[Any]=deque()
        inserir=input("\nDigite um número para inserção\n")
        queue.append(inserir)
        d=deque(inserir)
        cont+=1
        print(f'Contador :{cont} Elemento')
        print()
        while option!=5:
                print('''                [1]-Inserir 
                [2]-Remover
                [3]-Imprimir todos os elementos
                [4]-buscar
                [5]-Sair do programa fila- voltar ao menu anterior
                    ''')
                '''Escolha sua opção ou digite 5 Para sair!!'''
                option=int(input("Escolha uma opção ou digite (5)- para sair\n"))
                while option>5:
                    '''Erro! Digite de acordo com a númeração!'''
                    print("\nErro! Digite de acordo com a númeração\n")
                    print('''                    [1]-Inserir 
                    [2]-Remover
                    [3]-Imprimir
                    [4]-Buscar
                    [5]-Sair do programa fila- voltar ao menu anterior
                    ''')
                    '''Escolha sua opção ou digite 4 Para sair!!'''
                    option=int(input("Escolha uma opção ou digite (5)-para sair\n"))
                if option==1:
                        inserir=input("\nDigite um número para inserção\n")
                        queue.append(inserir)
                        d+=deque(inserir)
                        cont+=1
                        print("Contador: ", cont)
                ''' Na opção (2), o último elemento é removido e retornado, mostrado na tela'''
                if option==2:
                    cont-=1
                    ultimo_elemento_a_ser_removido=queue.popleft()
                    print(f'O último elemento a ser removido foi o {ultimo_elemento_a_ser_removido}')
                    print("Contador ", cont)
                ''' na opção (3), é mostrado todos os dados digitados'''
                if option==3:
                    print("\n___ Todos os Dados Digitados____\n")
                    for i in d:
                        print(f'elemento {i}')
                print("="*30)
                if option==4:
                    elemento=input("Busque o Elemento : ")
                    for item in d:
                        if elemento==item:
                            print("Elemento {0} está presente na lista!".format(item))
                        else:
                            print("Elemento {0} não foi digitado na busca e por isso não encontrado.".format(item))  
                if option==5:
                    '''Saindo do programa Lista'''
                    print("Saindo do Programa Lista\n")
                    sleep(2)
                    print("Saiu! :)")
    if option==2:
        print('\tBem-vindo ao programa\n ')
        sleep(2)
        stack: List[str] = []
        inserir=input("Digite um elemento para inserção\n")
        stack.append(inserir)
        cont+=1
        print("Contador : ",cont)
        class NodoLista:
            """ Esta classe representa um nodo de uma Lista Encadeada"""
            def __init__(self,dado=0, proximo_nodo=None):
                self.dado=dado
                self.proximo=proximo_nodo
            def __repr__(self):
                return '%s -> %s' % (self.dado, self.proximo)
        class ListaEncadeada:
            """ esta classe Representa uma lista encadeada"""
            def __init__(self):
                self.cabeca=None
            def __repr__(self):
                return "[" + str(self.cabeca) + "]"
        def insere_no_inicio(lista,novo_dado):
            # 1) Crie um novo nodo com o dado a ser armazernado.
            novo_nodo=NodoLista(novo_dado)
            #2) Faz com que o novo nodo seja a cabeça da Lista
            novo_nodo.proximo=lista.cabeca
            #3) Faz com que a cabeça da lista referencie o novo nodo.
            lista.cabeca=novo_nodo
        def insere_depois(lista,nodo_anterior, novo_dado):
            assert nodo_anterior, "Nodo anterior precisa existir na lista"
            #cria um novo nodo com o dado desejado.
            novo_nodo=NodoLista(novo_dado)
            #Faz o próximo do novo nodo ser o próximo do nodo anterior.
            novo_nodo.proximo=nodo_anterior.proximo
            #Faz com que o novo nodo seja o próximo do nodo anterior.
            nodo_anterior.proximo=novo_nodo
        def busca(lista, valor):
            corrente=lista.cabeca
            while corrente and corrente.dado !=valor:
                corrente=corrente.proximo
                return corrente
        lista=ListaEncadeada()
        insere_no_inicio(lista, inserir)
        print("Lista contém um único ELemento : ", lista)
        print("=>"*30)
        option=0
        while option!=5:
                print('''                
                [1]-Continuar inserido
                [2]-Remover
                [3]-Imprimir
                [4]-Buscar Elemento
                [5]-Sair do programa Pilha- voltar ao menu anterior
                    ''')
                '''Escolha sua opção ou digite 4 Para sair!!'''
                option=int(input("Escolha uma opção ou digite 5 para sair \n"))
                while option>5:
                    '''Erro! Digite de acordo com a númeração!'''
                    print("\nErro! Digite de acordo com a númeração\n")
                    print('''                       
                    [1]-continuar inserido
                    [2]-remover
                    [3]-imprimir
                    [4]-Buscar Elemento
                    [5]-Sair do programa Pilha- voltar ao menu anterior
                    ''')
                    '''Escolha sua opção ou digite 5 Para sair!!'''
                    option=int(input("Escolha uma opção ou digite 5 para sair\n"))
                if option==1:
                    inserir=input("Digite outro Elemento :")
                    nodo_anterior=lista.cabeca
                    insere_depois(lista,nodo_anterior,inserir)
                    stack.append(inserir)
                    cont+=1
                    print("Contador : ", cont)
                    print("Inserido um novo elemento depois de um outro :",lista)

                if option==2: # opção de retirada de elemento
                    try:
                        print(f'O elemento Retirado : {stack.pop()}')
                        cont-=1
                        print("Contador : ", cont)
                    except IndexError:
                        print("Sua pilha está vazia")
                    
                if option==3:
                    for book in stack[::-1]:
                                print(book)
                if option==4: # opção de busca
                    elemento=input("Busque o Elemento : ")
                    for item in  stack[::-1]:
                        if elemento==item:
                            print("Elemento {0} informado está presente na lista!".format(item))
                        else:
                            print("Elemento {0} não foi digitado na busca e por isso não encontrado.".format(item))
                if option==5:
                    print("Finalizando")
                    sleep(2)
                    print("Saiu do programa")
print("="*30)
