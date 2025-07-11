from GerenciadorDeTarefas.core.tarefas import Gerenciador_De_Tarefas


def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("5 - Editar tarefa")
    print("6 - Buscar tarefa por palavra-chave")
    print("0 - Sair")

def executar():
    """Função principal que executa o menu e coordena as ações."""
    gestor = Gerenciador_De_Tarefas()

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
                indice = int(input("Número da tarefa que deseja editar: "))
                nova = input("Nova descrição (ou digite 'cancelar' para voltar): ").strip()
                if nova.lower() in ["cancelar", "sair", "0"]:
                    print("🚫 Edição cancelada pelo usuário.")
                elif nova == "":
                    print("⚠️ Nenhuma descrição foi digitada.")
                else:
                    gestor.editar_tarefa(indice, nova.capitalize())
            except ValueError:
                print("⚠️ Por favor, insira um número válido.")
        elif opcao == "6":
            termo = input("Digite uma palavra para buscar nas tarefas: ").strip()
            gestor.buscar_tarefas(termo)



if __name__ == "__main__":
    executar()
