#exemplo
# Importando os módulos necessários
import csv
import json
from datetime import datetime

# --- Cenário: Simulação de um ciclo de operação em uma célula de manufatura ---

# 1. ESCREVENDO EM ARQUIVO DE TEXTO (.txt) - MODO 'w' (Write)
print("--- 1. Iniciando novo log de ciclo de produção ---")
with open("ciclo_log.txt", "w") as log_file:
    timestamp_inicio = datetime.now().isoformat()
    log_file.write(f"Ciclo de produção iniciado em: {timestamp_inicio}\n")
    log_file.write("Status: Célula de montagem energizada.\n")

print("Log inicial 'ciclo_log.txt' criado/sobrescrito.\n")

# 2. ADICIONANDO DADOS A UM ARQUIVO CSV - MODO 'a' (Append)
print("--- 2. Coletando e salvando dados de sensores em 'dados_sensor.csv' ---")
leituras_sensor = [
    {"temp": 45.2, "pressao": 1015},
    {"temp": 47.8, "pressao": 1012},
    {"temp": 49.1, "pressao": 1010}
]

with open("dados_sensor.csv", "a", newline="") as csv_file:
    fieldnames = ["timestamp", "temperatura_c", "pressao_mbar"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    for leitura in leituras_sensor:
        timestamp_leitura = datetime.now().isoformat()
        writer.writerow({
            "timestamp": timestamp_leitura,
            "temperatura_c": leitura["temp"],
            "pressao_mbar": leitura["pressao"]
        })
print("Novas leituras de sensor adicionadas a 'dados_sensor.csv'.\n")

# 3. SALVANDO ESTADO FINAL EM ARQUIVO JSON
print("--- 3. Salvando estado final da máquina em 'estado_final.json' ---")
estado_maquina = {
    "id_maquina": "MAQ-007",
    "timestamp_final": datetime.now().isoformat(),
    "ultimo_ciclo": {
        "id_lote": "LOTE-54B9",
        "pecas_produzidas": 1500,
        "pecas_rejeitadas": 3
    },
    "status_ferramentas": {
        "ferramenta_corte": "87% de vida útil",
        "ferramenta_solda": "calibrada"
    }
}

with open("estado_final.json", "w") as json_file:
    json.dump(estado_maquina, json_file, indent=4)

print("Estado final da máquina salvo em 'estado_final.json'.")