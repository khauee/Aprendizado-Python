def calcular_media_consumo(consumo_maquinas):
    if not consumo_maquinas:
        return "0.0"
    
    total=0
    
    for valor in consumo_maquinas.values():
        total+=valor
        
    return(total/len(consumo_maquinas))

print(calcular_media_consumo({"m1": 100, "m2": 200}))

