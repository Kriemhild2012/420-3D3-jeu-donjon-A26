# models/comportements/comportement_aleatoire.py
import random
from modeles.comportements.comportement import Comportement
from modeles.actions.action_attaque import ActionAttaque
from modeles.actions.action_defense import ActionDefense
from modeles.actions.action import Action


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> Action:
        return random.choice([ActionAttaque(), ActionDefense()])