# test_tarefas.py
from tarefas import GerenciadorDeTarefas

def test_listar_tarefas(capsys):
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [
        {"descrição": "Estudar", "Concluída": False},
        {"descrição": "Revisar código", "Concluída": True}
    ]

    gestor.listar_tarefas()
    output = capsys.readouterr().out

    assert "1. Estudar [❌ Pendente]" in output
    assert "2. Revisar código [✅ Concluída]" in output


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

def test_excluir_tarefa(monkeypatch):
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [{"descrição": "Apagar", "Concluída": False}]

    monkeypatch.setattr("builtins.input", lambda _: "s")  # Simula confirmação
    gestor.excluir_tarefa(1)

    assert len(gestor.tarefas) == 0

    
def test_editar_tarefa(monkeypatch):
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [{"descrição": "Antiga", "Concluída": False}]

    monkeypatch.setattr("builtins.input", lambda _: "s")  # Simula confirmação
    gestor.editar_tarefa(1, "Atualizada")

    assert gestor.tarefas[0]["descrição"] == "Atualizada"


def test_concluir_tarefa(monkeypatch):
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [{"descrição": "Exemplo", "Concluída": False}]
    
    monkeypatch.setattr("builtins.input", lambda _: "s")  # Simula confirmação "s"
    
    gestor.concluir_tarefa(1)
    assert gestor.tarefas[0]["Concluída"] is True
    
def test_buscar_tarefas(capsys):
    gestor = GerenciadorDeTarefas()
    gestor.tarefas = [
        {"descrição": "Estudar Python", "Concluída": False},
        {"descrição": "Revisar projeto", "Concluída": True},
        {"descrição": "Estudar matemática", "Concluída": False}
    ]

    gestor.buscar_tarefas("estudar")
    output = capsys.readouterr().out

    assert "1. Estudar Python" in output
    assert "3. Estudar matemática" in output
    assert "2. Revisar projeto" not in output


    