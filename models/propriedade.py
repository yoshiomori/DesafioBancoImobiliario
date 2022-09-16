from models.jogador import Jogador


class Propriedade(object):
    def __init__(self, custo_de_venda: int, valor_de_aluguel: int, proprietario: Jogador = None) -> None:
        super().__init__()
        self.custo_de_venda = custo_de_venda
        self.valor_de_aluguel = valor_de_aluguel
        self.proprietario = proprietario
