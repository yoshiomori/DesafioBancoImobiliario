import random


FACES = (1, 2, 3, 4, 5, 6)


class Dado(object):
    def __init__(self) -> None:
        super().__init__()
        self.face_para_cima = 1

    def lancar(self):
        self.face_para_cima = random.choice(FACES)
