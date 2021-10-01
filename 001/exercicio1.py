#Ler uma lista de 5 números inteiros e mostre cada número juntamente com sua posição na lista.
i=0
list=[]
while i<5:
    valor=int(input("Informe o valor:" ))
    list.append(valor)
    i+=1
for i, word in enumerate(list):
        print('na posição',i,'foi digitado o número ',word)
