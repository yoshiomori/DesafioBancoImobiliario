def compra_propriedade(jogador, propriedade):
    propriedade.proprietario = jogador
    jogador.saldo -= propriedade.custo_de_venda
