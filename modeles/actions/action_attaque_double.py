# modeles/actions/action_attaque_double.py
from modeles.actions.action import Action
 
 
class ActionAttaqueDouble(Action):
 
    def appliquer(self, ennemi, heros_hp: int, action_heros: str) -> tuple[int, str]:
        degats = ennemi.attaque * 2
        if action_heros == "defend":
            degats = degats // 2
            msg = f"  → {ennemi.nom} attaque en BERSERK — vous vous défendez ! Seulement {degats} dégâts reçus."
        else:
            msg = f"  → {ennemi.nom} attaque en BERSERK pour {degats} dégâts !"
        return max(0, heros_hp - degats), msg