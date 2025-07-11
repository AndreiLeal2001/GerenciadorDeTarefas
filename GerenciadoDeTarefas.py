#PROJETO -- GERENCIADOR DE TAREFAS --
# menu (opções)
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    @staticmethod
    def exibir_opcoes():
        print("\n--- MENU ---")
        print("1- LISTAR TAREFAS:")
        print("2- ADICIONAR TAREFA:")
        print("3- CONCLUIR TAREFA:")
        print("4- EXCLUIR TAREFA:")
        print("5- SALVAR TAREFA:")
        print("0- SAIR...")

        # 1. LISTAR TAREFA
    def listar_tarefas(self):
        print("\n📋 Tarefas:")
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada no momento.")
        for i, tarefa in enumerate(self.tarefas, start=1):
            descricao = tarefa.get('descrição', 'Sem descrição')
            status = "✅" if tarefa.get("Concluída", False) else "❌"
            print(f"{i} - {descricao} [{status}]")


        # 2. ADICIONAR TAREFA
    def adicionar_tarefa(self, descricao):
        self.tarefas.append({"descrição": descricao, "Concluída": False})
        print("Tarefa adicionada!")

        # 3. CONCLUIR TAREFA
    def concluir_tarefa(self, indice):
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["Concluída"] = True
            print("Tarefa concluída!")
        else:
            print("ERROR:001... Essa tarefa não é um dicionário.")

        # 4. EXCLUIR TAREFA
    def excluir_tarefa(self, indice):
        indice -= 1
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            print("Tarefa excluída!")

        # 5. SALVAR TAREFA

    def executar(self):
        while True:
            self.exibir_opcoes()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_tarefas()
            elif opcao == "2":
                descricao = input("Descrição da tarefa: ")
                self.adicionar_tarefa(descricao)
            elif opcao == "3":
                indice = int(input("Índice da tarefa para concluir: "))
                self.concluir_tarefa(indice)
            elif opcao == "4":
                indice = int(input("Índice da tarefa para excluir: "))
                self.excluir_tarefa(indice)
            elif opcao == "5":
                ''
            elif opcao == "0":
                print("ENCERRANDO O PROGRAMA...")
                break
            else:
                print("Opção inválida. Tente Novamente.")

app = GerenciadorDeTarefas()
app.executar()


