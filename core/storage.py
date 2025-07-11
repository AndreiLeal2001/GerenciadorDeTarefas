import json
import os

ARQUIVO = "tarefas.json"

def salvar_tarefas(tarefas):
    """Salvar a lista de tarefas em formato JSON."""
    with open(ARQUIVO, 'w', encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    """Carregar as tarefas do arquivo JSON, se exisitir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []