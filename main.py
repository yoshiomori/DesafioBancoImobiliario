import argparse

from controller.executa_simulacao import executa_simulacao
from views.imprime_na_mesma_linha import imprime_na_mesma_linha
from views.print_resultado import print_resultado


def main():
    parser = argparse.ArgumentParser(prog='Banco Imobiliário')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    n_timeout = 0
    turnos = []
    qnt_vitorias_por_tipo = dict()
    n_simulacoes = 0
    while n_simulacoes < 300:
        n_simulacoes += 1
        turno, jogador_vitorioso = executa_simulacao(args)
        tipo_do_jogador_vitorioso = jogador_vitorioso.__class__.__name__
        qnt_vitorias_por_tipo.setdefault(tipo_do_jogador_vitorioso, 0)
        qnt_vitorias_por_tipo[tipo_do_jogador_vitorioso] += 1
        if turno >= 1000:
            n_timeout += 1
        turnos.append(turno)
        imprime_na_mesma_linha(n_simulacoes)
    print_resultado(n_timeout, qnt_vitorias_por_tipo, turnos)


if __name__ == '__main__':
    main()
