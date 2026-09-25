# models/comportements/comportement_furtif.py
from modeles.comportement import Comportement


class ComportementFurtif(Comportement):

    def __init__(self) -> None:
        self._tour = 0   # ← valeur initiale ?

    def agir(self, ennemi) -> str:
        self._tour += 1
        if self._tour % 2 == 0:
            return "attaque"
        return "defend"