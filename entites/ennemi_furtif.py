# entites/ennemi_furtif.py
import random
from entites.ennemi import Ennemi


class EnnemiFurtif(Ennemi):
    """Alterne entre attaque et défense à chaque tour."""

    def __init__(self, nom: str, hp: int, attaque: int) -> None:
        super().__init__(nom, hp, attaque)   # ← appel au constructeur parent
        self._tour = 0                 # ← valeur initiale ?

    def agir(self) -> str:
        self._tour += 1
        if self._tour % 2 == 0:
            return "defend"
        return "attaque"