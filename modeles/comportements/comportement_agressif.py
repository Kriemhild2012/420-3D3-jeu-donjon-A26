# entites/ennemi_agressif.py
from entites.ennemi import Ennemi


class EnnemiAgressif(Ennemi):
    """Attaque à chaque tour, sans exception."""

    def agir(self) -> str:
        return "attaque"