from modeles.ennemi_agressif import EnnemiAgressif
from modeles.ennemi_defensif import EnnemiDefensif
from modeles.ennemi_aleatoire import EnnemiAleatoire
from modeles.ennemi_furtif import EnnemiFurtif

ennemis = [
    EnnemiAgressif("Goblin",  hp=50,  attaque=8),
    EnnemiDefensif("Dragon",  hp=100, attaque=12),
    EnnemiAleatoire("Spectre", hp=40, attaque=10),
    EnnemiFurtif("Voleur",   hp=30,  attaque=10),
]