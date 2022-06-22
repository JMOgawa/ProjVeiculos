#Projeto Veículos

placas=[]
marcas=[]
modelos=[]
anos=[]
precos=[]
tipos=[]
soma_cam=0
soma_car=0
soma_mt=0
cont=0
c=int(input("Quantos veículos vendidos você deseja cadastrar?: "))
for i in range(c):
    pl=input("Digite a placa: ")
    placas.append(pl)
    mc=input("Digite a marca: ")
    marcas.append(mc)
    md=input("Digite o modelo: ")
    modelos.append(md)
    an=int(input("Digite o ano: "))
    anos.append(an)
    pr=float(input("Digite o preço: "))
    precos.append(pr)
    tp=input("Digite o tipo: ")
    tipos.append(tp)
    
for i in range(c):
    if i==0:
        menor = maior = precos[i]
    elif precos[i] > maior:
        maior=precos[i]
    elif precos[i] < menor:
        menor=precos[i]
print("Menor Preço: ", menor)
print("Maior Preço: ", maior)
precos.append(menor)
y=precos.index(menor)
print("Dados do veículo mais barato ")
print("PLACA:", placas[y], "MARCA:", marcas[y], "MODELO:", modelos[y])
print("ANO:", anos[y], "PREÇO:", precos[y], "TIPO:", tipos[y], "\n")
precos.append(maior)
x=precos.index(maior)
print("Dados do veículo mais caro ")
print("PLACA:", placas[x], "MARCA:", marcas[x], "MODELO:", modelos[x])
print("ANO:", anos[x], "PREÇO:", precos[x], "TIPO:", tipos[x], "\n")

pergt=input("De qual tipo de veículo você deseja ver a média de preços?: ")
if pergt=='caminhão' or pergt=='Caminhão':
    for i in range(c):
        cam1=tipos.count('caminhão')
        cam2=tipos.count('Caminhão')
        total_cam=cam1+cam2
        if tipos[i]=='caminhão'or tipos[i]=='Caminhão':
            soma_cam=soma_cam+precos[i]    
    media_cam=soma_cam/total_cam
    print("Média de Preços dos Caminhões: %.2f" %media_cam, "\n")
elif pergt=='moto' or pergt=='Moto':
    for i in range(c):
        mt1=tipos.count('moto')
        mt2=tipos.count('Moto')
        total_mt=mt1+mt2
        if tipos[i]=='moto' or tipos[i]=='Moto':
            soma_mt=soma_mt+precos[i]
    media_mt=soma_mt/total_mt
    print("Média de Preços das Motos: %.2f" %media_mt, "\n")
elif pergt=='carro' or pergt=='Carro':
    for i in range(c):
        car1=tipos.count('carro')
        car2=tipos.count('Carro')
        total_car=car1+car2
        if tipos[i]=='carro' or tipos[i]=='Carro':
            soma_car=soma_car+precos[i]
    media_car=soma_car/total_car    
    print("Média de Preços dos Carros: %.2f" %media_car, "\n")
    
for i in range(c):
    cont=cont+1
    print("Dados do Veículo ", cont)
    print("PLACA:", placas[i], "MARCA:", marcas[i], "MODELO:", modelos[i])
    print("ANO:", anos[i], "PREÇO:", precos[i],"TIPO:", tipos[i], "\n")