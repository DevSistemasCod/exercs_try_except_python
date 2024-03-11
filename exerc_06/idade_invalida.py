class IdadeInvalida(ValueError):
    def __init__(self, message="Idade inválida."):
        super().__init__(message)