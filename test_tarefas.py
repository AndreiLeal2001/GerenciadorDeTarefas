# test_tarefas.py
from tarefas import GerenciadorDeTarefas

def test_adicionar_tarefa():
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = []  # limpando para teste isolado
    gestor.adicionar_tarefa("Estudar Python")
    
    assert len(gestor.tarefas) == 1
    assert gestor.tarefas[0]["descrição"] == "Estudar Python"
    assert gestor.tarefas[0]["Concluída"] is False

def test_concluir_tarefa():
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [{"descrição": "Testar", "Concluída": False}]
    gestor.concluir_tarefa(1)
    
    assert gestor.tarefas[0]["Concluída"] is True

def test_excluir_tarefa():
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [{"descrição": "Excluir", "Concluída": False}]
    gestor.excluir_tarefa(1)
    
    assert len(gestor.tarefas) == 0
    
def test_editar_tarefa():
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [{"descrição": "Tarefa antiga", "Concluída": False}]
    