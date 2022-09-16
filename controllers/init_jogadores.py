from models.jogador import JogadorImpulsivo, JogadorExigente, JogadorCauteloso, JogadorAleatorio


def init_jogadores():
    return (
        JogadorImpulsivo(),
        JogadorExigente(),
        JogadorCauteloso(),
        JogadorAleatorio(),
    )
