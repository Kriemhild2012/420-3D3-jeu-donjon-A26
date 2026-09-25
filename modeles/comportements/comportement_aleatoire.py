# models/comportements/comportement_aleatoire.py
import random
from modeles.comportements.comportement import Comportement


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> str:
        return random.choice(["attaque", "defend"])