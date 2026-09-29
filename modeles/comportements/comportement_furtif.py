# models/comportements/comportement_furtif.py
from modeles.comportements.comportement import Comportement
from modeles.actions.action_attaque import ActionAttaque
from modeles.actions.action_defense import ActionDefense
from modeles.actions.action import Action



class ComportementFurtif(Comportement):

    def __init__(self) -> None:
        self._tour = 0   # ← valeur initiale ?

    def agir(self, ennemi) -> Action:
        self._tour += 1
        if self._tour % 2 == 0:
            return ActionAttaque()
        return ActionDefense()
        
        