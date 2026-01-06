# Passo 1: A Palavra-Chave 'class' - O Início do Projeto
class ValvulaControle:
    """
    Esta classe modela uma Válvula de Controle Proporcional,
    um componente crucial em sistemas de automação industrial para
    regular o fluxo de fluidos.
    """

    # Passo 2: O Construtor '__init__' - A Linha de Montagem do Objeto
    def __init__(self, id_valvula, tipo_fluido):
        # Passo 3: Atributos - As Propriedades de Cada Válvula
        print(f"CRIANDO nova válvula com ID: {id_valvula}")
        self.id_valvula = id_valvula
        self.tipo_fluido = tipo_fluido
        self.abertura_percentual = 0.0
        self.status = "operacional"

    # Passo 4: Métodos - Os Comportamentos da Válvula
    def ajustar_abertura(self, percentual_desejado):
        """Ajusta a posição da válvula para um novo percentual."""
        if 0 <= percentual_desejado <= 100:
            self.abertura_percentual = float(percentual_desejado)
            print(f"[{self.id_valvula}] Abertura ajustada para {self.abertura_percentual}%.")
        else:
            print(f"[{self.id_valvula}] ERRO: Abertura deve ser entre 0 e 100.")

    def relatar_estado(self):
        """Retorna uma string formatada com o estado atual da válvula."""
        estado = (f"--- Relatório da Válvula {self.id_valvula} ---\n"
                  f"  Fluido: {self.tipo_fluido}\n"
                  f"  Abertura: {self.abertura_percentual}%\n"
                  f"  Status: {self.status}\n"
                  f"------------------------------------")
        return estado

# --- Fim do Projeto (Classe) ---

# Passo 5: Instanciação - Fabricando os Objetos
print("--- Iniciando sistema de controle de fluidos ---")
valvula_agua_tanque = ValvulaControle("V-101", "Água Resfriada")
valvula_ar_compressor = ValvulaControle("V-25A", "Ar Comprimido")
print("-" * 20)

# Passo 6: Utilização - Colocando os Objetos para Trabalhar
valvula_agua_tanque.ajustar_abertura(75.5)
valvula_ar_compressor.ajustar_abertura(100)
print("-" * 20)
print(valvula_agua_tanque.relatar_estado())
print(valvula_ar_compressor.relatar_estado())

# Tentando um ajuste inválido
valvula_agua_tanque.ajustar_abertura(110)