from tarefas import GerenciadorDeTarefas


def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Editar tarefa")
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
            descricao = input("Digite a descrição da tarefa:\n(ou 'cancelar', 'voltar', 'sair', '0' para desistir)\n> ").strip()

        # Cancelamento direto
            if descricao.lower() in ["cancelar", "voltar", "sair", "0"]:
                print("❌ Criação cancelada. Voltando ao menu principal...")
            elif descricao == "":
                print("⚠️ Você não digitou nenhuma descrição.")
            else:
                # Confirmação antes de salvar
                confirmacao = input(f"Você deseja salvar a tarefa: \"{descricao}\"? (s/n)\n> ").strip().lower()
            if confirmacao == "s":
                gestor.adicionar_tarefa(descricao.capitalize())
            else:
                print("🚫 Tarefa não foi criada. Retornando ao menu...")
    
        elif opcao == "3":
            try:
                indice = int(input("Digite o número da tarefa que deseja concluir: "))
                gestor.concluir_tarefa(indice)
            except ValueError:
                    print("⚠️ Por favor, digite um número válido.")

        elif opcao == "4":
            try:
                indice = int(input("Digite o número da tarefa que deseja excluir: "))
                gestor.excluir_tarefa(indice)
            except ValueError:
                print("⚠️ Por favor, digite um número válido.")

        
        elif opcao == "5":
            try:
                indice = int(input("Índice da tarefa que deseja editar:"))
                nova_descricao = input("Nova descrição da tarefa: ")
                gestor.editar_tarefa(indice, nova_descricao)
            except ValueError:
                print("Digite um número válido.")
        
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
