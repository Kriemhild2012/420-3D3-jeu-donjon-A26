# modeles/comportements/comportement_agressif.py
from modeles.comportements.comportement import Comportement
from modeles.actions.action_attaque import ActionAttaque
from modeles.actions.action import Action
 
class ComportementAgressif(Comportement):
    def agir(self, ennemi) -> Action:
        return ActionAttaque()