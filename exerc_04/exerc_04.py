def exibir_menu():
    print("\nMenu:")
    print("1 - Adicionar chave e valor")
    print("2 - Remover chave")
    print("3 - Sair")

def adicionar_chave_valor(dicionario):
    continuar = True

    while continuar:
        try:
            chave = int(input("Informe a chave: "))
            continuar = False
        except ValueError:
            print("Entrada inválida. A chave deve ser um número inteiro. Tente novamente.")

    valor = input(f"Informe o valor para a chave '{chave}': ")
    dicionario[chave] = valor
    print(f"Chave '{chave}' adicionada com sucesso.")


def remover_chave(dicionario):
    continuar = True

    while continuar:
        try:
            chave = int(input("Informe a chave para remover: "))
            continuar = False
        except ValueError:
            print("Entrada inválida. A chave deve ser um número inteiro. Tente novamente.")

    try:
        del dicionario[chave]
        print(f"Chave '{chave}' removida com sucesso.")
    except KeyError:
        print(f"Erro: Chave '{chave}' não encontrada no dicionário.")

    
def operacoes_em_dicionario(dicionario):
    while True:
        exibir_menu()
        escolha = int(input("Escolha uma opção (1, 2 ou 3): "))

        if escolha == 1:
            adicionar_chave_valor(dicionario)
            print("Dicionário atualizado:", dicionario)
        elif escolha == 2:
            remover_chave(dicionario)
            print("Dicionário atualizado:", dicionario)
        elif escolha == 3:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    meu_dicionario = {1: "Python", 2:"Java", 3:"C#"}
    print(" Meu dicionário Atual: ",meu_dicionario)
    operacoes_em_dicionario(meu_dicionario)
