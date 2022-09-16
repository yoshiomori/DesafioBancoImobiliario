import random


class Jogador(object):
    def __init__(self) -> None:
        super().__init__()
        self.posicao_no_tabuleiro = 0
        "Os jogadores sempre começam uma partida com saldo de 300 para cada um"
        self.saldo = 300

    def competitivo(self):
        """Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto
podem ser compradas por qualquer outro jogador."""
        return self.saldo >= 0

    def estrategia_compra(self, propriedade):
        from models.propriedade import Propriedade
        assert isinstance(propriedade, Propriedade)
        return propriedade.custo_de_venda < self.saldo


class JogadorImpulsivo(Jogador):
    def estrategia_compra(self, propriedade):
        """O jogador impulsivo compra qualquer propriedade sobre a qual ele parar."""
        return super().estrategia_compra(propriedade)


class JogadorExigente(Jogador):
    def estrategia_compra(self, propriedade):
        """O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50."""
        return super().estrategia_compra(propriedade) and propriedade.valor_de_aluguel > 50


class JogadorCauteloso(Jogador):
    def estrategia_compra(self, propriedade):
        """O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
depois de realizada a compra."""
        from models.propriedade import Propriedade
        assert isinstance(propriedade, Propriedade)
        return propriedade.custo_de_venda + 80 <= self.saldo


class JogadorAleatorio(Jogador):
    def estrategia_compra(self, propriedade):
        """O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%."""
        return super().estrategia_compra(propriedade) and random.choice((True, False))
