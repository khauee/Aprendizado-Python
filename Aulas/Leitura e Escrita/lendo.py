#exemplo 
# Importando os módulos necessários para CSV e JSON
import csv
import json

# --- Cenário: Simulação de inicialização de um Gateway IoT ---

# Primeiro, vamos simular a existência dos arquivos que nosso programa irá ler.
# Em um cenário real, esses arquivos já estariam no dispositivo.

# Arquivo 1: device_id.txt (Texto Simples)
with open("device_id.txt", "w") as f:
    f.write("GW-I40-BR-031")

# Arquivo 2: sensor_log.csv (CSV)
with open("sensor_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "vibration_x", "vibration_y"])
    writer.writerow(["1678886400", "0.51", "1.20"])
    writer.writerow(["1678886401", "0.53", "1.22"])
    writer.writerow(["1678886402", "0.95", "1.89"]) # Anomalia

# Arquivo 3: config.json (JSON)
config_data = {
    "network": {
        "wifi_ssid": "FactoryFloor_Net",
        "wifi_pass": "senhaSuperSegura123"
    },
    "server": {
        "host": "data.minhafabrica.com",
        "port": 8883
    },
    "active_sensors": ["Temperature", "Vibration"]
}
with open("config.json", "w") as f:
    json.dump(config_data, f, indent=4)

print("--- Arquivos de simulação criados. Iniciando leitura. ---\n")

# 1. LENDO ARQUIVO DE TEXTO SIMPLES (.txt)
print("--- 1. Lendo ID do Dispositivo de 'device_id.txt' ---")
try:
    with open("device_id.txt", "r") as file:
        device_id = file.read().strip()
        print(f"ID do Gateway lido com sucesso: {device_id}\n")
except FileNotFoundError:
    print("ERRO: Arquivo de ID não encontrado!\n")

# 2. LENDO ARQUIVO CSV
print("--- 2. Processando Log de Sensor de 'sensor_log.csv' ---")
try:
    with open("sensor_log.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(f"Cabeçalho do CSV: {header}")
        for row in csv_reader:
            timestamp = int(row[0])
            vib_x = float(row[1])
            if vib_x > 0.9:
                print(f"ALERTA: Vibração anômala detectada no timestamp {timestamp}: {vib_x}")
    print("\n")
except FileNotFoundError:
    print("ERRO: Arquivo de log do sensor não encontrado!\n")

# 3. LENDO ARQUIVO JSON
print("--- 3. Carregando Configurações de 'config.json' ---")
try:
    with open("config.json", "r") as file:
        config = json.load(file)
        server_host = config["server"]["host"]
        active_sensors = config["active_sensors"]
        print(f"Gateway configurado para enviar dados para: {server_host}")
        print(f"Sensores ativos na configuração: {active_sensors}\n")
except FileNotFoundError:
    print("ERRO: Arquivo de configuração não encontrado!\n")
except json.JSONDecodeError:
    print("ERRO: O arquivo de configuração está mal formatado (não é um JSON válido)!\n")