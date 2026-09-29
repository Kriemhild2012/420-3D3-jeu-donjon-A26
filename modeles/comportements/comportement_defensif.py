# models/comportements/comportement_defensif.py
from modeles.comportements.comportement import Comportement
from modeles.actions.action_defense import ActionDefense
from modeles.actions.action import Action

 
class ComportementDefensif(Comportement):
    def agir(self, ennemi) -> Action:
        return ActionDefense()