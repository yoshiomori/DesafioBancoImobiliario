import decimal

from views.imprime_na_mesma_linha import imprime_na_mesma_linha


def print_resultado(n_timeout, qnt_vitorias_por_tipo, turnos):
    imprime_na_mesma_linha(f"Quantas partidas terminam por time out (1000 rodadas): {n_timeout}")
    print(f'Quantos turnos em média demora uma partida: {decimal.Decimal(sum(turnos)) / len(turnos)}')
    print(
        f'Qual a porcentagem de vitórias por comportamento dos jogadores: {";".join(f"{decimal.Decimal(v) / 300}({t})" for t, v in qnt_vitorias_por_tipo.items())}')
    print(f'Qual o comportamento que mais vence: {max(qnt_vitorias_por_tipo)}')