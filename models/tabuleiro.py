from models.propriedade import Propriedade


class Tabuleiro(object):
    def __init__(self) -> None:
        super().__init__()
        self.propriedades = (
            Propriedade(10, 5),
            Propriedade(60, 55),
            Propriedade(10, 5),
            Propriedade(60, 55),
            Propriedade(10, 5),
            Propriedade(30, 25),
            Propriedade(10, 5),
            Propriedade(10, 5),
            Propriedade(60, 55),
            Propriedade(10, 5),
            Propriedade(10, 5),
            Propriedade(60, 55),
            Propriedade(10, 5),
            Propriedade(30, 25),
            Propriedade(10, 5),
            Propriedade(10, 5),
            Propriedade(10, 5),
            Propriedade(60, 55),
            Propriedade(10, 5),
            Propriedade(10, 5),
        )
        self.numero_de_propriedades_no_tabuleiro = len(self.propriedades)

    def limpa_tabuleiro(self):
        """Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto
podem ser compradas por qualquer outro jogador."""
        for propriedade in self.propriedades:
            if propriedade.proprietario:
                if not propriedade.proprietario.competitivo():
                    propriedade.proprietario = None
