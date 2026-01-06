new_list = []
def filtrar_leituras_acima_limite(leituras, limite):
    for leitura in leituras:
        if leitura > limite:
            new_list.append(leitura)
    
    return(new_list)

print(filtrar_leituras_acima_limite([10, 20, 30, 40], 25))
