class CadastroDuplicado(Exception):
    def __init__(self, message="Cadastro duplicado."):
        super().__init__(message)