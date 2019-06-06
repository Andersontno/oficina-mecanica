class CpfNaoEncontradoException(BaseException):
    def __init__(self,cpf):
        super().__init__()
        self.cpf = cpf
    def __str__(self):
        return "O CPF \""+str(self.cpf)+"\" NAO ESTA CADASTRADO!!!"