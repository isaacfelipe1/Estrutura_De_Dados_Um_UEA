#9-Faça um programa que leia um número indeterminado de notas. Após esta entrada de dados, faça seguinte:
#. Mostre a quantidade de notas que foram lidas.
#. Exiba todas as notas na ordem em que foram informadas.
#. Calcule e mostre a média das notas.
#. Calcule e mostre a quantidade de notas acima da média calculada.
list=[]
acima_media=[]
notas=float(input("Informe suas notas(-1 para sair\n"))
while(notas>=0):
    list.append(notas)
    notas=float(input("Informe suas notas(-1 para sair\n"))
media=sum(list)/len(list)
for i, word in enumerate(list):
    if word>media:
        acima_media+=[word]
        soma=len(acima_media)
    print('na posição',i,'foi digitado o número ',word)
print(f' A quantidades de notas que foram informados:  {len(list)}')
print()
print('=>'*30)
print(f'A média das notas foi {media}')
print(f'{soma}')

print(acima_media)