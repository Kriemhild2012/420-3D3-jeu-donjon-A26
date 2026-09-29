# models/comportements/comportement_berserker.py
from modeles.comportements.comportement import Comportement
from modeles.actions.action_attaque import ActionAttaque
from modeles.actions.action_attaque_double import ActionAttaqueDouble
from modeles.actions.action import Action
 
 
class ComportementBerserker(Comportement):
 
    def agir(self, ennemi) -> Action:
        if ennemi.hp < ennemi.hp_max * 0.3:
            return ActionAttaqueDouble()
        return ActionAttaque()