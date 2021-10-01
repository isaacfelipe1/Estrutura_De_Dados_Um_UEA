#8- Faça um programa que crie uma matriz M com valores informados do usuário) mostre a matriz com o dobro dos valores (2*m)
m=[]
usuario=int(input("Informe a quantidade da matriz\n"))
for i in range(usuario):
    m.append([0]*usuario*2)
    m[i][i]=1
print(m)

