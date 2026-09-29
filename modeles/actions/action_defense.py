# modeles/actions/action_defense.py
from modeles.actions.action import Action
 
 
class ActionDefense(Action):
 
    def appliquer(self, ennemi, heros_hp: int, action_heros: str) -> tuple[int, str]:
        return heros_hp, f"  → {ennemi.nom} se défend."