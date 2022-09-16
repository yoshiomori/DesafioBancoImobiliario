def paga_aluguel(jogador, propriedade):
    jogador.saldo -= propriedade.valor_de_aluguel
    propriedade.proprietario.saldo += propriedade.valor_de_aluguel
