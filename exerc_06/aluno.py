from cadastro_duplicados import CadastroDuplicado
from idade_invalida import IdadeInvalida
from nome_invalido import NomeInvalido
from notas_invalidas import NotasInvalidas

class Aluno:
    def __init__(self, nome, idade, notas):
        self.__nome = nome
        self.__idade = idade
        self.__notas = notas

    def cadastrar_aluno(self, lista_alunos):
        try:
            self.validar_nome()
            self.validar_idade()
            self.validar_notas()

            if self in lista_alunos:
                raise CadastroDuplicado("Erro: Aluno já cadastrado.")

            lista_alunos.append(self)
            print("Cadastro realizado com sucesso!")

        except NomeInvalido as e:
            print(f"Erro durante o cadastro - Nome Inválido: {e}")
        except IdadeInvalida as e:
            print(f"Erro durante o cadastro - Idade Inválida: {e}")
        except NotasInvalidas as e:
            print(f"Erro durante o cadastro - Notas Inválidas: {e}")
        except CadastroDuplicado as e:
            print(f"Erro durante o cadastro - Cadastro Duplicado: {e}")

    def exibir_aluno(self):
        print(f"\nAluno:")
        print(f"Nome: {self.__nome}, Idade: {self.__idade}, Notas: {self.__notas}")

    def validar_nome(self):
        if not isinstance(self.__nome, str):
            raise NomeInvalido("Nome deve ser uma string.")

        if len(self.__nome) < 3:
            raise NomeInvalido("Nome deve ter pelo menos 3 caracteres.")

        for char in self.__nome:
            if char.isdigit():
                raise NomeInvalido("Nome não pode conter números.")

    def validar_idade(self):
        if not isinstance(self.__idade, int):
            raise IdadeInvalida("Idade deve ser um número inteiro.")

        if not (0 < self.__idade < 120):
            raise IdadeInvalida("Idade deve ser maior que 0 e menor que 120.")


    def validar_notas(self):
        for nota in self.__notas:
            if not isinstance(nota, (int, float)):
                raise NotasInvalidas("As notas devem ser números inteiros ou decimais.")
        
            if not (0 <= nota <= 10):
                raise NotasInvalidas("Cada nota deve estar no intervalo de 0 a 10.")

    # usado para comparar se os objetos são identicos
    def __eq__(self, other):
        if isinstance(other, Aluno):
            return (
                self.__nome == other.__nome and 
                self.__idade == other.__idade and
                self.__notas == other.__notas
            )
        return False
