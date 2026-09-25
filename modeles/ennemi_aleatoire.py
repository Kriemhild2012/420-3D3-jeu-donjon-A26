# entites/ennemi_aleatoire.py
import random
from entites.ennemi import Ennemi


class EnnemiAleatoire(Ennemi):
    """Choisit aléatoirement entre attaquer et défendre."""

    def agir(self) -> str:
        return random.choice(["attaque", "defend"])