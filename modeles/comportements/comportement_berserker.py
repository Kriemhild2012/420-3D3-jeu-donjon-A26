# models/comportements/comportement_agressif.py
from modeles.comportements.comportement import Comportement


class ComportementBerserker(Comportement):

    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return "attaque_berserker"
        return "attaque"