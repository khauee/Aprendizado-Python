#Definindo dicionário

estado_maquina = {
    "maquina_1": "operacional",
    "maquina_2": "manuntenção",
    "maquina_3": "parada",
    "maquina_4": "operacional"
}

print(f"O estado das maquinas são: {estado_maquina}")#Acessando todos os valores

estado_maquina.update({"maquina_5": "operacional"})#Acrescenta objeto

print(f"O estado da maquina 1 é: ", estado_maquina["maquina_1"])#Acessando valor específico
print(f"O estado das maquinas são: {estado_maquina}")

del estado_maquina["maquina_5"]#Remove objeto
tam = {len(estado_maquina)}#tamanho

print(f"O estado das maquinas são: {estado_maquina}")
print(tam)
print(f"Máquinas atualmente registradas: {estado_maquina.keys()}")
