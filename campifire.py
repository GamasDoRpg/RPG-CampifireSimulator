import random
import time

lenha = 0
regeneracao = 0
sanidade = 100
perda_sanidade = 0
consumo_fogueira = 0
risco_ataque = 0
luz = 0
ferimentos = 0
condicao_fisica = 100

def narrar(texto, delay=1.5):
    print(texto)
    time.sleep(delay)

def dificuldade():
    global perda_sanidade, regeneracao, lenha_inicial, risco_ataque, consumo_fogueira
    
    narrar("\n CAMPIFIRE S1MULATOR ")
    narrar("Selecione a dificuldade:")
    narrar("A dificuldade define fatores como perda de sanidade, regeneração, risco e recursos iniciais.\n")
    
    narrar("1 - Fácil       → Perda mínima de sanidade, regeneração alta, muita lenha por perto.")
    narrar("2 - Normal      → Equilibrado, moderada perda de sanidade, recursos razoáveis.")
    narrar("3 - Difícil     → Perda rápida de sanidade, recursos escassos.")
    narrar("4 - Sobrevivente→ Quase nenhum recurso inicial, sanidade cai rápido.")
    narrar("5 - Insano      → Mínima margem para erro, sanidade despenca, inimigos mais agressivos.")
    
    escolha = input("\nEscolha (1-5): ")
    
    if escolha == "1":  # Fácil
        perda_sanidade = 1
        regeneracao = 5
        lenha = 10
        risco_ataque = 0.05
        consumo_fogueira = 1
        
    elif escolha == "2":  # Normal
        perda_sanidade = 2
        regeneracao = 3
        lenha_inicial = 7
        risco_ataque = 0.15
        consumo_fogueira = 2
        
    elif escolha == "3":  # Difícil
        perda_sanidade = 3
        regeneracao = 2
        lenha_inicial = 5
        risco_ataque = 0.25
        consumo_fogueira = 3
        
    elif escolha == "4":  # Sobrevivente
        perda_sanidade = 4
        regeneracao = 1
        lenha_inicial = 3
        risco_ataque = 0.35
        consumo_fogueira = 3
        
    elif escolha == "5":  # Insano
        perda_sanidade = 5
        regeneracao = 0
        lenha_inicial = 2
        risco_ataque = 0.5
        consumo_fogueira = 4
        
    else:
        narrar("Opção inválida. Usando dificuldade Normal por padrão.")
        perda_sanidade = 2
        regeneracao = 3
        lenha_inicial = 7
        risco_ataque = 0.15
        consumo_fogueira = 2
    
    narrar(f"\nDificuldade definida. Lenha inicial: {lenha_inicial}, Perda de sanidade/turno: {perda_sanidade}, Regeneração: {regeneracao}.")
  
