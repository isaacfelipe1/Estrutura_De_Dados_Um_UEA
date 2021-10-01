#.10- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As Perguntas são:
#- “Telefonou para a Vítima? ”
#- “Esteve no local do crime? ”
#-“Mora perto da Vítima? ”
#-“ Tinha Dívidas com a vítima? ”	
#-“ Já trabalhou com a vítima? ”
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “SUSPEITA”; entre 3 e 4 como “ CÚMPLICE” e; 5 como “ASSASINO”. Caso contrário, ele será classificado como “INOCENTE”.
list=[]
pn1=int(input("Telefonou para a Vítima? 1-(sim) 0-(não)"))
list.append(pn1)
pn2=int(input("Esteve no local do crime? 1-(sim) 0-(não)"))#pergunta de número dois
list.append(pn2)
pn3=int(input("Mora perto da Vítima? 1-(sim) 0-(não)"))#pergunta de número 3
list.append(pn3)
pn4=int(input("Tinha Dívidas com a vítima? 1-(sim) 0-(não)"))#pergunta de número 4
list.append(pn4)
pn5=int(input("Já trabalhou com a vítima? 1-(sim) 0-(não)"))#pergunta de número5
list.append(pn5)
contra1=list.count(1)
if contra1==2:
    print("suspeito")
if contra1==3 or contra1==4:
    print("Cúmplice")
if contra1==5 :
    print("Assasino")
if contra1!=2 and contra1!=3 and contra1!=4 and contra1!=5 and contra1!=1 and contra1==0 :
    print("Inocente")


