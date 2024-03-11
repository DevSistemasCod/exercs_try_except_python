class NomeInvalido(ValueError):
    def __init__(self, message="Nome inválido."):
        super().__init__(message)