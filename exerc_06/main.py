from aluno import Aluno

if __name__ == "__main__":
    alunos_cadastrados = []

    aluno1 = Aluno("Carlos", 19, [8.5, 9.0, 7.5])
    aluno1.cadastrar_aluno(alunos_cadastrados)

    aluno2 = Aluno("Pedro", 20, [9.2, 8.7, 7.8])
    aluno2.cadastrar_aluno(alunos_cadastrados)

    aluno3 = Aluno("Lucas", 22, [7.0, 6.5, 8.0])
    aluno3.cadastrar_aluno(alunos_cadastrados)

    aluno4 = Aluno("Lucas", 22, [7.0, 6.5, 8.0])  # Causa exceção de cadastro duplicado
    aluno4.cadastrar_aluno(alunos_cadastrados)

    aluno5 = Aluno("Ana", -5, [7.5, 8.0, 6.5])  # Causa exceção de idade inválida
    aluno5.cadastrar_aluno(alunos_cadastrados)

    aluno6 = Aluno("Cleber", 28, [7.5, "A", 6.5])  # Causa exceção de notas inválidas
    aluno6.cadastrar_aluno(alunos_cadastrados)

    for aluno in alunos_cadastrados:
        aluno.exibir_aluno()
