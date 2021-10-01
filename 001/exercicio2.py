#2- Ler uma lista de 10 números reais e mostre-os na ordem inversa.
list=[]
i=0
while i<10:
    valor=float(input("Informe o valor:" ))
    list.append(valor)
    i+=1
list.reverse()
i=0
print()
print("Os valores de forma reverso são\n")
for i in list:
    print(i)