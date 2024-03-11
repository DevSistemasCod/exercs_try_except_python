class NotasInvalidas(ValueError):
    def __init__(self, message="Notas inválidas."):
        super().__init__(message)