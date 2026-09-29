# models/comportement.py
from abc import ABC, abstractmethod
from modeles.actions.action import Action


class Comportement(ABC):

    @abstractmethod
    def agir(self, ennemi) -> Action:
        """Décide l'action de l'ennemi pour ce tour.

        Args:
            ennemi : l'ennemi qui agit (pour accéder à ses HP, etc.)

        Returns:
            Action
        """
        pass