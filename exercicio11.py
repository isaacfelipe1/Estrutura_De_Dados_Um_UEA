#11- Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande quantidade de organizações: ”. Qual o melhor sistema operacional para uso em servidores? ” As Possíveis respostas são:
#1-Windows XP 2- Unix 3- Linux 4- Netware 5 – Mac Os 6- outro
#Você deve desenvolver um programa em Python que leia as respostas da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0 (zero), que encerra a entrada dos dados. Não deverão ser aceitos valores além dos números válidos para o programa (0 a 6).
#os valores referentes a cada uma das opções devem ser armazenados em uma lista. após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada uma das respostas e informar o vencedor da enquete.

Contador=0
list=[]
cont=0
print("\n Qual é o melhor sistema operacional para uso de servidores ? : ")
print("\n1-windows XP 2-Unix 3- Linux 4- netware 5- Mac Os 6- outro\n" )
print()
resposta=int(input("Informe sua resposta"))
if resposta<6:
        list.append(resposta)
        cont=cont+1
print("=>"*30)
while resposta >6:
    print("Erro! para votar, digite os valores de acordo com a númeração abaixo\n")
    print()
    print("\n1-windows XP 2-Unix 3- Linux 4- netware 5- Mac Os 6- outro\n" )
    print()
    resposta=int(input("Informe sua resposta"))
    if resposta<6:
            list.append(resposta)
            cont=cont+1
while (resposta!=0):
        print("\n Continue votando ou digite 0(zero) para sair ")
        print("\n1-windows XP 2-Unix 3-Linux 4-netware 5-Mac Os 6- outro\n" )
        print()
        resposta=int(input("Informe sua resposta"))
        list.append(resposta)
        cont=cont+1
        #if resposta==0:
            #list.remove(0)
            #print("\n Cessão encerada! Obrigado por votar!\n")
contar1=list.count(1)
percentual1=contar1/100
contar2=list.count(2)
percentual2=contar2/100
contar3=list.count(3)
percentual3=contar3/100
contar4=list.count(4)
percentual4=contar4/100
contar5=list.count(5)
percentual5=contar5/100
contar6=list.count(6)
percentual6=contar6/100
print("=>"*30)
print()
print(">="*30)
print()
print("___________ operacionais-votos%_____\n")
print(f'(1-windows XP ) {contar1} ,{percentual1} %\n')
print(f'(2-unix) {contar2} ,{percentual2} %\n')
print(f'(3-linux ) {contar3} ,{percentual3} %\n')
print(f'(4-Netware ) {contar4} ,{percentual4} %\n')
print(f'(5-Mac Os) {contar5} ,{percentual5} %\n')
print(f'(6-Outros) {contar6} ,{percentual6} %\n')
print()
print(">="*30)
print(f'Total de {cont-1} votos')
print()
print("\n...... O sistema Operacional que foi mais votado.........\n")
if contar1>contar2 and contar1>contar3 and  contar1>contar4 and contar1>contar5 and contar1>contar6:
    print(f'O sistema Operacional mais votado foi o (1-windows XP ), com {contar1} votos , correspondendo a {percentual1} % dos votos')
elif contar2>contar1 and contar2>contar3 and  contar2>contar4 and contar2>contar5 and contar2>contar6:
    print(f'O sistema Operacional mais votado foi o (2-Unix ), com {contar2} votos , correspondendo a {percentual2} % dos votos')
elif contar3>contar1 and contar3>contar2 and  contar3>contar4 and contar3>contar5 and contar3>contar6:
    print(f'O sistema Operacional mais votado foi o (3-linux), com {contar3} votos , correspondendo a {percentual3} % dos votos')
elif contar4>contar1 and contar4>contar2 and  contar4>contar3 and contar4>contar5 and contar4>contar6:
    print(f'O sistema Operacional mais votado foi o (4-Netware), com {contar4} votos , correspondendo a {percentual4} % dos votos')
elif contar5>contar1 and contar5>contar2 and  contar5>contar3 and contar5>contar4 and contar5>contar6:
    print(f'O sistema Operacional mais votado foi o (5-Mac Os), com {contar5} votos , correspondendo a {percentual5} % dos votos')
elif contar6>contar1 and contar6>contar2 and  contar6>contar3 and contar6>contar4 and contar6>contar5:
      print(f'O sistema Operacional mais votado foi o (6-Outros), com {contar6} votos , correspondendo a {percentual6} % dos votos')
else:
    print("Total de votos foi igual para todos os sistemas operacionais\n")
print(">="*30)



