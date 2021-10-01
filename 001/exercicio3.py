#3- Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

list=[]
notas=0
media=0
soma=0
while notas<4:
    notas_alunos=float(input("Informe a nota\n"))
    list.append(notas_alunos)
    notas+=1
def menu():
    for i in list:
        print("As notas foram : ", i)
        media=sum(list)/len(list) 
    print("sua média foi : ", media)

menu()
