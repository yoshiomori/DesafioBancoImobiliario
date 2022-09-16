def jogo_valendo(rodada, numero_de_jogadores_competitivos):
    if rodada >= 1000:
        """Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada
        com a vitória do jogador com mais saldo."""
        return False
    if numero_de_jogadores_competitivos <= 1:
        return False
    return True
