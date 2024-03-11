def validar_nome(nome):
    if not nome.isalpha():
        raise TypeError("O nome deve ser uma string.")

def verificar_nome_curto(nome):
    if len(nome) < 3:
        raise ValueError("O nome deve ter pelo menos 3 caracteres.")

def cadastro():
    continuar = True
    while continuar:
        try:
            nome = input("Informe seu nome: ")

            # Validar se o nome é uma string
            validar_nome(nome)

            # Verificar se o nome é curto
            verificar_nome_curto(nome)

            # Se tudo estiver correto, exibir uma mensagem de sucesso
            print(f"Nome válido: {nome}")
            continuar = False

        except (TypeError) as e:
            print(f"Erro: {e}")
        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    cadastro()
