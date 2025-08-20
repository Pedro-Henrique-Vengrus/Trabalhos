class Acao:
    def executarAcao(self):
        raise NotImplementedError("Error.")


class SalvarArquivo(Acao):
    def executarAcao(self):
        print("Arquivo salvo com sucesso!")


class ImprimirDocumento(Acao):
    def executarAcao(self):
        print("Documento enviado para a impressora.")


class EnviarEmail(Acao):
    def executarAcao(self):
        print("E-mail enviado com sucesso!")


def executar(acao: Acao):
    acao.executarAcao()


acoes = [SalvarArquivo(), ImprimirDocumento(), EnviarEmail()]

for acao in acoes:
    executar(acao)
