#5- Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PARES e IMPAR 
list=[]
par=[]
impar=[]
contador=0
while contador<20:
    list.append(contador)
    contador+=1
print("\n...........Números pares.............\n")
for i in list:
    if i%2==0:
        par=[i]
        print(par)
print("\n...... números impares..........\n")

for i in list:
    if i%2!=0:
        impar=[i]
        print(impar)