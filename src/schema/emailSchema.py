

class EmailSchema(object):
    def __init__(self, request) -> None:
        self.request = request

    def validator(self):
        errorMensages = []

        try:
            self.nome = self.request.get("nome", None)
            if self.nome is None or len(self.nome) <= 1:
                raise Exception("Error")
        except Exception as e:
            errorMensages.append("Fiel name is required")

        try:
            self.email = self.request.get("email", None)
            if self.email is None or len(self.email) <= 1:
                raise Exception("Error")
        except Exception as e:
            errorMensages.append("Fiel email is required")

        try:
            self.assunto = self.request.get("assunto", None)
            if self.assunto is None or len(self.assunto) <= 1:
                raise Exception("Error")
        except Exception as e:
            errorMensages.append("Fiel assunto is required")

        try:
            self.mensagem = self.request.get("conteudo", None)
            if self.mensagem is None or len(self.mensagem) <= 1:
                raise Exception("Error")
        except Exception as e:
            errorMensages.append("Fiel mensagem is required")

        return errorMensages

    def descontruct(self):
        return self.nome, self.email, self.assunto, self.mensagem
