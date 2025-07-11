from storage import salvar_tarefas, carregar_tarefas

class GerenciadorDeTarefas:
    """
    Classe responsável por gerenciar uma lista de tarefas.
    Cada tarefa é representada como um dicionário com:
        - 'descrição' (str)
        - 'Concluída' (bool)
    """

    def __init__(self):
        """Inicializa a lista de tarefas vazia."""
        self.tarefas = carregar_tarefas()

    def listar_tarefas(self):
        """
        Exibe todas as tarefas cadastradas com status visual.
        Se não houver tarefas, informa ao usuário.
        """
        print("\n📋 Tarefas:")

        if not self.tarefas:
            print("🕳️ Nenhuma tarefa cadastrada no momento.")
            return

        for i, tarefa in enumerate(self.tarefas, start=1):
            try:
                descricao = tarefa.get("descrição", "Sem descrição")
                status = "✅ Concluída" if tarefa.get("Concluída", False) else "❌ Pendente"
                print(f"{i}. {descricao} [{status}]")
            except AttributeError:
                print(f"{i}. ❌ ERRO: formato inesperado de tarefa.")


    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa à lista."""
        self.tarefas.append({"descrição": descricao, "Concluída": False})
        salvar_tarefas(self.tarefas)
        print("Tarefa adicionada!")

    def concluir_tarefa(self, indice):
        """
        Marca uma tarefa como concluída, após confirmação.
        Parâmetro:
        - indice (int): Índice da tarefa (começando em 1)
        """
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            print(f"Tarefa selecionada: {tarefa['descrição']} [Concluída: {tarefa['Concluída']}]")
            confirmar = input("Deseja marcar como concluída? (s/n): ").strip().lower()
            if confirmar == "s":
                tarefa["Concluída"] = True
                salvar_tarefas(self.tarefas)
                print("✅ Tarefa marcada como concluída!")
            else:
                print("🚫 Ação cancelada. Tarefa não foi modificada.")
        else:
            print("❌ Índice inválido. Tarefa inexistente.")


    def editar_tarefa(self, indice, nova_descricao):
        """
        Atualiza a descrição de uma tarefa existente.
        Parâmetros:
            - indice (int) - Posição da tarefa(començando em 1).
            - nova_descrição(str) - Texto atualizado para a tarefa.
        """
        indice -= 1 # Ajusta para índice interno da lista
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["descrição"] = nova_descricao
            salvar_tarefas(self.tarefas) #Atualiza o arquivo com as tarefas
            print("Tarefa atualizada!")
        else:
            print("Índice inválido. Não foi possível atualizar a tarefa.")

    def excluir_tarefa(self, indice):
        """
        Remove uma tarefa da lista, com confirmação.
        Parâmetro:
        - indice (int): Posição da tarefa (começando em 1)
        """
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            print(f"Tarefa selecionada: {tarefa['descrição']} [Concluída: {tarefa['Concluída']}]")
            confirmar = input("Tem certeza que deseja excluir essa tarefa? (s/n): ").strip().lower()
            if confirmar == "s":
                del self.tarefas[indice]
                salvar_tarefas(self.tarefas)
                print("🗑️ Tarefa excluída com sucesso.")
            else:
                print("🚫 Exclusão cancelada. Nenhuma tarefa foi removida.")
        else:
            print("❌ Índice inválido. Tarefa inexistente.")

