from modeles.ennemi import Ennemi
from modeles.comportements.comportement_agressif import ComportementAgressif
from modeles.comportements.comportement_defensif import ComportementDefensif
from modeles.comportements.comportement_aleatoire import ComportementAleatoire
from modeles.comportements.comportement_furtif import ComportementFurtif

ennemis = [
    Ennemi("Goblin",  hp=50,  attaque=8,  comportement=ComportementAgressif()),
    Ennemi("Dragon",  hp=100, attaque=12, comportement=ComportementDefensif()),
    Ennemi("Spectre", hp=40,  attaque=10, comportement=ComportementAleatoire()),
    Ennemi("Voleur",  hp=30,  attaque=10, comportement=ComportementFurtif()),
]