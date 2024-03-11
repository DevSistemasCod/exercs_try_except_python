def verificar_idade():
    continuar = True
    while continuar:
        try:
            idade = int(input("Informe sua idade: "))
        except ValueError:
            print("Erro: Valor inválido. Certifique-se de inserir um número inteiro para a idade.")
        else:
            if 18 <= idade <= 120:
                print("Idade válida. Você está dentro do intervalo.")
                continuar = False
            else:
                print("Idade inválida. Certifique-se de inserir uma idade entre 18 e 120 anos.")

if __name__ == "__main__":
    verificar_idade()

