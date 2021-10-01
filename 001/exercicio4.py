#4- Ler um vetor com 29 idades e exibir a maior e menor.

list=[]
contador=0
maior=0
menor=0
while contador<29:
    idade=int(input("Informe sua idade\n"))
    list.append(idade)
    maior=max(list)
    menor=min(list)
    contador+=1
print("O maior número: ", maior)
print("O menor valor: ", menor)