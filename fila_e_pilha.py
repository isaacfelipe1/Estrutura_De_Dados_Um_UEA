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
                    stack.append(inserir)
                    cont+=1
                    print("Contador : ", cont)
                if option==2: # opção de retirada de elemento
                    try:
                        print(f'O elemento Retirado : {stack.pop()}')
                        cont-=1
                        print("Contador : ", cont)
                    except IndexError:
                        print("Sua pilha está vazia")
                    
                if option==3:
                    for i in stack[::-1]:
                                print(i)
                if option==4: # opção de busca
                    elemento=input("Busque o Elemento : ")
                    for i in  stack[::-1]:
                        if elemento==i:
                            print("Elemento {0} informado está presente na lista!".format(i))
                        else:
                            print("Elemento {0} não foi digitado na busca e por isso não encontrado.".format(i))
                if option==5:
                    print("Finalizando")
                    sleep(2)
                    print("Saiu do programa")
print("="*30)
