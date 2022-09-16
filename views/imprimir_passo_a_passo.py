from time import sleep

from views.imprime_na_mesma_linha import imprime_na_mesma_linha


def imprimir_passo_a_passo(jogadores, tabuleiro):
    imprime_na_mesma_linha(
        ' '.join(
            f"{''.join([f'{jogadores.index(jogador)}({jogador.saldo})' for jogador in jogadores if jogador.posicao_no_tabuleiro == index])}:{f'{jogadores.index(propriedade.proprietario)}' if propriedade.proprietario else '-'}"
            for index, propriedade in enumerate(tabuleiro.propriedades))
    )
    sleep(3)
