# models/comportements/comportement_agressif.py
from modeles.comportements.comportement import Comportement


class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return "attaque"