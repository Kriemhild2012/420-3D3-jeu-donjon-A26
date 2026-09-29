# models/comportement.py
from abc import ABC, abstractmethod


class Comportement(ABC):

    @abstractmethod
    def agir(self, ennemi) -> str:
        """Décide l'action de l'ennemi pour ce tour.

        Args:
            ennemi : l'ennemi qui agit (pour accéder à ses HP, etc.)

        Returns:
            "attaque" ou "defend"
        """
        pass