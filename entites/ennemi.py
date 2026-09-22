# entites/ennemi.py
from abc import ABC, abstractmethod


class Ennemi(ABC):

    def __init__(self, nom: str, hp: int, attaque: int) -> None:
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque

    @abstractmethod
    def agir(self) -> str:
        """Décide l'action de cet ennemi pour ce tour."""
        pass

    def recevoir_degats(self, degats: int) -> None:
        self.hp = max(0, self.hp - degats)

    def est_vivant(self) -> bool:
        return self.hp > 0

    def __str__(self) -> str:
        return f"{self.nom} (HP: {self.hp}/{self.hp_max})"