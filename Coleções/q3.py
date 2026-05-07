def adicionar_contato(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome] = telefone
        print(f"   Telefone de '{nome}' atualizado para {telefone}.")
    else:
        agenda[nome] = telefone
        print(f"   Contato '{nome}' adicionado com sucesso.")


def buscar_telefone(agenda, nome):
    if nome in agenda:
        print(f"   {nome}: {agenda[nome]}")
    else:
        print(f"  Contato '{nome}' não encontrado.")


def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"   Contato '{nome}' removido com sucesso.")
    else:
        print(f"  Contato '{nome}' não encontrado.")


def listar_contatos(agenda):
    if not agenda:
        print("  A agenda está vazia.")
        return

    print(f"\n  {'Nome':<25} {'Telefone':<15}")
    print("  " + "-" * 40)
    for nome, telefone in sorted(agenda.items()):
        print(f"  {nome:<25} {telefone:<15}")
    print("  " + "-" * 40)
    print(f"  Total: {len(agenda)} contato(s).")




def exibir_menu():
    print("\n" + "=" * 40)
    print(f"{'  AGENDA DE CONTATOS':^40}")
    print("=" * 40)
    print("  [1] Adicionar contato")
    print("  [2] Buscar telefone")
    print("  [3] Remover contato")
    print("  [4] Listar contatos")
    print("  [5] Sair")
    print("=" * 40)


def main():
    agenda = {}

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("  Nome: ").strip()
            telefone = input("  Telefone: ").strip()
            if nome and telefone:
                adicionar_contato(agenda, nome, telefone)
            else:
                print("  ⚠ Nome e telefone não podem ser vazios.")

        elif opcao == "2":
            nome = input("  Nome a buscar: ").strip()
            buscar_telefone(agenda, nome)

        elif opcao == "3":
            nome = input("  Nome a remover: ").strip()
            remover_contato(agenda, nome)

        elif opcao == "4":
            listar_contatos(agenda)

        elif opcao == "5":
            print("\n  Até logo! \n")
            break

        else:
            print(" Opção inválida. Escolha entre 1 e 5.")


if __name__ == "__main__":
    main()