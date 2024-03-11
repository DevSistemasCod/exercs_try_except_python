class Contato:
    def __init__(self, nome, cpf, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, E-mail: {self.__email}"

    # Método para validar
    def validar_email(self):
        try:
        # Verifica se o novo e-mail possui o formato desejado
            if ("@" not in self.__email) or ("." not in self.__email) or ("com" not in self.__email):
                print("Formato de e-mail inválido!")
                print("Por favor, verifique o formato e tente novamente.")
            else:
                print("E-mail atualizado com sucesso.")

        except TypeError as e:
            print(f"Erro: {e}. \n Por favor, verifique o formato e tente novamente.")
            self.atualizar_email()

        except Exception as e:
            print(f"Erro capturado: {e}. \n Por favor, tente novamente.")
            self.atualizar_email()


    def atualizar_email(self):
        continuar = True

        while continuar:
            novo_email = input("Informe o novo e-mail: ")

            # Verifica se o novo e-mail possui o formato desejado
            if ("@" not in novo_email) or ("." not in novo_email) or ("com" not in novo_email):
                print("Formato de e-mail inválido. Por favor, verifique o formato e tente novamente.")
            else:
                self.__email = novo_email
                print("E-mail atualizado com sucesso.")
                continuar = False
