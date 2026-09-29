# modeles/actions/action_attaque.py
from modeles.actions.action import Action
 
 
class ActionAttaque(Action):
 
    def appliquer(self, ennemi, heros_hp: int, action_heros: str) -> tuple[int, str]:
        if action_heros == "defend":
            degats = ennemi.attaque // 2
            msg = f"  → {ennemi.nom} attaque — vous vous défendez ! Seulement {degats} dégâts reçus."
        else:
            degats = ennemi.attaque
            msg = f"  → {ennemi.nom} vous attaque pour {degats} dégâts !"
        return max(0, heros_hp - degats), msg