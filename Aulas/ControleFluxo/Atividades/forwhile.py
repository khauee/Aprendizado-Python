'''#for -> percorre listas e tuplas
i=0

for i in range (10):#range-> gera sequencia de valores
    print("Produto", i+1, "verificado")

#while

temperatura = 15

while temperatura <= 30:
    print(f"Temperatura atual: {temperatura:.2f} C°")
    temperatura+=1

for i in range(1, 10, 2): #Vai de 1 a 9 pulando de 2 em 2
    print(range)

# for em dicionário
consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}


for setor, consumo in consumo_setores.items():

    if consumo > 100:
      status = "acima do limite" 
    else:
      status = "dentro do limite"
    # Exibe o setor, o consumo e o status
    print(f"Setor: {setor} | Consumo: {consumo} kW – Status: {status}")'''

consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}

for sensor in consumo_setores: print(sensor)