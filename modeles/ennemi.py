# models/ennemi.py
from modeles.comportements.comportement import Comportement
from modeles.actions.action import Action


class Ennemi:

    def __init__(self, nom: str, hp: int, attaque: int,
                 comportement: Comportement,
                 regles_adaptation=None) -> None:
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self._comportement = comportement   # ← composition
        self._regles_adaptation = regles_adaptation or []   # ← liste, vide par défaut

    def agir(self) -> Action:
        return self._comportement.agir(self)   # ← délégation

    def set_comportement(self, comportement: Comportement) -> None:
        self._comportement = comportement       # ← remplacement

    def get_comportement(self) -> Comportement:
        return self._comportement

    def recevoir_degats(self, degats: int) -> None:
        self.hp = max(0, self.hp - degats)
        if not self.est_vivant():
            return
        else:
            for regle in self._regles_adaptation:
                regle(self)

    def est_vivant(self) -> bool:
        return self.hp > 0

    def __str__(self) -> str:
        return f"{self.nom} (HP: {self.hp}/{self.hp_max})"