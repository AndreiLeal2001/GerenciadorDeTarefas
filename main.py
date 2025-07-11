from tarefas import GerenciadorDeTarefas

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

def executar():
    """Função principal que executa o menu e coordena as ações."""
    gestor = GerenciadorDeTarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gestor.listar_tarefas()
        elif opcao == "2":
            descricao = input("Descrição da tarefa: ")
            gestor.adicionar_tarefa(descricao)
        elif opcao == "3":
            try:
                indice = int(input("Índice da tarefa para concluir: "))
                gestor.concluir_tarefa(indice)
            except ValueError:
                print("Digite um número válido.")
        elif opcao == "4":
            try:
                indice = int(input("Índice da tarefa para excluir: "))
                gestor.excluir_tarefa(indice)
            except ValueError:
                print("Digite um número válido.")
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
