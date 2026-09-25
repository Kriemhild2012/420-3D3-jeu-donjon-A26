from entites.ennemi_agressif import EnnemiAgressif
from entites.ennemi_defensif import EnnemiDefensif
from entites.ennemi_aleatoire import EnnemiAleatoire
from entites.ennemi_furtif import EnnemiFurtif

ennemis = [
    EnnemiAgressif("Goblin",  hp=50,  attaque=8),
    EnnemiDefensif("Dragon",  hp=100, attaque=12),
    EnnemiAleatoire("Spectre", hp=40, attaque=10),
    EnnemiFurtif("Voleur",   hp=30,  attaque=10),
]