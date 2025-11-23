import pyperclip  # Para acessar a área de transferência
import pyautogui  # Para simular a digitação
import time       # Para pausas

# --- CONFIGURAÇÃO ---
# Tempo de espera (em segundos) que você tem para CLICAR no campo de texto 
# do site Redação Paraná após rodar o script.
TEMPO_ESPERA = 5 

print("--- AUTOMAÇÃO DE DIGITAÇÃO INICIADA ---")

# 1. OBTENÇÃO DO TEXTO
try:
    # Obtém o texto da área de transferência
    texto_a_digitar = pyperclip.paste()
    
    if not texto_a_digitar:
        print("🛑 ERRO: A área de transferência está vazia.")
        print("Copie o texto da sua redação e execute o script novamente.")
        # Termina o script
        exit()
        
    print(f"✅ Texto copiado com sucesso ({len(texto_a_digitar)} caracteres).")

except Exception as e:
    print(f"🛑 ERRO ao acessar a área de transferência: {e}")
    exit()

# 2. EXECUÇÃO DA AUTOMAÇÃO
print(f"\n⏳ A automação começará em {TEMPO_ESPERA} segundos.")
print(">>> CLIQUE NO CAMPO DE TEXTO DO REDAÇÃO PARANÁ AGORA! <<<")

# Pausa para o usuário posicionar o cursor no campo
time.sleep(TEMPO_ESPERA)

try:
    # Simula a digitação letra por letra. 
    # O interval=0.01 define 10 milissegundos de pausa entre cada tecla.
    # Você pode aumentar esse valor para uma digitação mais lenta e "humana".
    pyautogui.typewrite(texto_a_digitar, interval=0.01) 
    
    print("\n✅ Digitação concluída com sucesso!")

except pyautogui.FailSafeException:
    # Segurança: se você mover o mouse para o canto superior esquerdo durante a execução, 
    # o pyautogui interrompe o processo.
    print("❌ Automação interrompida pelo usuário (Fail-Safe ativado).")
except Exception as e:
    print(f"❌ Ocorreu um erro durante a digitação: {e}")