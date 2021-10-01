#7- Faça um programa que crie uma matriz aleatoriamente.
#O tamanho da matriz deve ser informado pelo usuári0
m=[]
usuario=int(input("Informe o tamanho da matriz\n"))
for i in range(usuario):
    m.append([0]*usuario)
    m[i][i]=1
print(m) 