from controllers.compra_propriedade import compra_propriedade
from controllers.init_jogadores import init_jogadores
from controllers.jogo_valendo import jogo_valendo
from controllers.paga_aluguel import paga_aluguel
from controllers.premio import premio
from models.dadoEquiprovavel6faces import Dado
from models.jogador import Jogador
from models.tabuleiro import Tabuleiro
from views.imprimir_passo_a_passo import imprimir_passo_a_passo


def executa_simulacao(args):
    """Inicializa o Tabuleiro"""
    tabuleiro = Tabuleiro()
    jogadores = init_jogadores()
    dado = Dado()
    rodada = 0
    numero_de_jogadores_competitivos = 4
    while jogo_valendo(rodada, numero_de_jogadores_competitivos):
        for jogador in filter(Jogador.competitivo, jogadores):
            dado.lancar()
            jogador.posicao_no_tabuleiro += dado.face_para_cima
            if jogador.posicao_no_tabuleiro >= tabuleiro.numero_de_propriedades_no_tabuleiro:
                """Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo"""
                premio(jogador, tabuleiro)
            propriedade = tabuleiro.propriedades[jogador.posicao_no_tabuleiro]
            if propriedade.proprietario is not None and propriedade.proprietario != jogador:
                paga_aluguel(jogador, propriedade)
                if not jogador.competitivo():
                    numero_de_jogadores_competitivos -= 1
                    tabuleiro.limpa_tabuleiro()
            elif propriedade.proprietario is None:
                if jogador.saldo > propriedade.custo_de_venda:
                    if jogador.estrategia_compra(propriedade):
                        compra_propriedade(jogador, propriedade)
        if args.verbose:
            imprimir_passo_a_passo(jogadores, tabuleiro)
        rodada += 1
    """Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada
com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta
partida."""
    return rodada, max(jogadores, key=lambda jogador: jogador.saldo)