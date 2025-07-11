from storage import salvar_tarefas, carregar_tarefas
from utils import logger


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

    def buscar_tarefa(self, palavra_chave):
        """
        Exibe tarefas que contenham a palavra-chave fornecida.
        Parâmetro:
        - Palavra_chave (str): termo a ser pesquisado na descrição.
        """
        termo = palavra_chave.strip().lower()
        if not termo:
            print("⚠️ Nenhuma palavra-chave foi fornecida.")
            return
        
        resultados = [
            (i + 1, tarefa) for i, tarefa in enumerate(self.tarefas) if termo in tarefa.get("descrição", "").lower()
        ]
        
        if resultados:
            print(f"\n🔍 Resultados para \"{palavra_chave}\":")
            for i, tarefa in resultados:
                status = "✅ Concluída" if tarefa.get("Concluída", False) else "❌ Pendente"
                print(f"{i}. {tarefa['descrição']} [{status}]")

    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa à lista."""
        self.tarefas.append({"descrição": descricao, "Concluída": False})
        salvar_tarefas(self.tarefas)
        logger.info("Nova tarefa adicionada: %s", descricao)
        print("✅ Tarefa adicionada!")

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
        Atualiza a descrição de uma tarefa, com confirmação do usuário.
        Parâmetros:
            - indice (int): Índice da tarefa (começando em 1)
            - nova_descricao (str): Texto atualizado
        """
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            print(f"Tarefa atual: \"{tarefa['descrição']}\" [Concluída: {tarefa     ['Concluída']}]")
            confirmar = input(f"Deseja alterar para: \"{nova_descricao}\"? (s/n): ").strip().lower()
            if confirmar == "s":
                tarefa["descrição"] = nova_descricao
                salvar_tarefas(self.tarefas)
                print("✏️ Tarefa editada com sucesso!")
            else:
                print("🚫 Edição cancelada.")
        else:
            print("❌ Índice inválido. Nenhuma tarefa editada.")

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

