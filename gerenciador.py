def exibir_menu():
    print("\n========================================")
    print("      GERENCIADOR DE TAREFAS (PYTHON)   ")
    print("========================================")
    print("1. Adicionar nova tarefa")
    print("2. Ver tarefas salvas")
    print("3. Sair")

def adicionar_tarefa():
    tarefa = input("\nDigite a descrição da tarefa: ")
    # Abre o arquivo 'tarefas.txt' no modo append ('a' - para adicionar sem apagar o anterior)
    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(tarefa + "\n")
    print("-> Tarefa salva com sucesso!")

def listar_tarefas():
    print("\n--- SUAS TAREFAS ---")
    try:
        # Tenta abrir o arquivo para leitura
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()
            if not tarefas:
                print("Nenhuma tarefa cadastrada ainda.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa.strip()}")
    except FileNotFoundError:
        print("Nenhuma tarefa cadastrada ainda (arquivo não encontrado).")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("\nEncerrando o programa. Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha entre 1 e 3.")

if __name__ == "__main__":
    main()
