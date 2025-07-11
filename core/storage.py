import json
import os

# Caminho absoluto até a pasta /data (um nível acima de /core)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
ARQUIVO = os.path.join(DATA_DIR, 'tarefas.json')

# Garante que a pasta /data existe
os.makedirs(DATA_DIR, exist_ok=True)

def salvar_tarefas(tarefas):
    """Salvar a lista de tarefas em formato JSON."""
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    """Carregar as tarefas do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []