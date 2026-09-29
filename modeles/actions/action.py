# modeles/actions/action.py
from abc import ABC, abstractmethod
 
 
class Action(ABC):
 
    @abstractmethod
    def appliquer(self, ennemi, heros_hp: int, action_heros: str) -> tuple[int, str]:
        """Applique l'action et retourne (nouveaux_hp_heros, message)."""
        pass