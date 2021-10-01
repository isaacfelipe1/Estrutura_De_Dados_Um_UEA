#6-Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorram (mostrar o mês por extenso: 1- janeiro, 2- fevereiro...).



list=[]
Contador=1
media=0
mostra=[]
while Contador<=12:
    temperatura=float(input("Informe a temperatura de cada mês \n"))
    list.append(temperatura)
    soma=sum(list)
    media=soma/12
    Contador+=1
print("\n.......Resultado...........")
for i, Contador in enumerate(list):
    if Contador>media:
            if i==0 and Contador>media:
                print("janeiro")
                mostra.append(Contador)
            if i==1 and Contador>media:
                print("fevereiro")
                mostra.append(Contador)
            elif i==2 and Contador>media:
                print("março")
                mostra.append(Contador)
            elif i==3 and Contador>media:
                print("abril")
                mostra.append(Contador)
            elif i==4 and Contador>media:
                print("maio")
                mostra.append(Contador)
            elif i==5 and Contador>media:
                print("junior")
                mostra.append(Contador)
            elif i==6 and Contador>media:
                print("julho")
                mostra.append(Contador)
            elif i==7 and Contador>media:
                print("agosto")
                mostra.append(Contador)
            elif i==8 and Contador>media:
                print("setembro")
                mostra.append(Contador)
            elif i==9 and Contador>media:
                print("outubro")
                mostra.append(Contador)
            elif i==10 and Contador>media:
                print("Novembro")
                mostra.append(Contador)
            elif i==11 and Contador>media:
                print("Dezembro")
                mostra.append(Contador)

print(media)
print("")
print(mostra)




    