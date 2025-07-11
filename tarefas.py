class GerenciadorDeTarefas:
    """
    Classe responsável por gerenciar uma lista de tarefas.
    Cada tarefa é representada como um dicionário com:
        - 'descrição' (str)
        - 'Concluída' (bool)
    """

    def __init__(self):
        """Inicializa a lista de tarefas vazia."""
        self.tarefas = []

    def listar_tarefas(self):
        """Exibe todas as tarefas cadastradas, com status de conclusão."""
        print("\n📋 Tarefas:")
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        for i, tarefa in enumerate(self.tarefas, start=1):
            descricao = tarefa.get("descrição", "Sem descrição")
            status = "✅" if tarefa.get("Concluída", False) else "❌"
            print(f"{i} - {descricao} [{status}]")

    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa à lista."""
        self.tarefas.append({"descrição": descricao, "Concluída": False})
        print("Tarefa adicionada!")

    def concluir_tarefa(self, indice):
        """
        Marca uma tarefa como concluída.
        Parâmetro: indice (int) — índice da tarefa fornecido pelo usuário (começando em 1).
        """
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["Concluída"] = True
            print("Tarefa concluída!")
        else:
            print("Essa tarefa não existe.")

    def excluir_tarefa(self, indice):
        """
        Remove uma tarefa da lista.
        Parâmetro: indice (int) — índice da tarefa fornecido pelo usuário (começando em 1).
        """
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            print("Tarefa excluída!")
        else:
            print("Índice inválido.")
