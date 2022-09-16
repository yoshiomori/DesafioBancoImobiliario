def premio(jogador, tabuleiro):
    jogador.saldo += 100
    jogador.posicao_no_tabuleiro = jogador.posicao_no_tabuleiro % tabuleiro.numero_de_propriedades_no_tabuleiro