# modeles/regles_adaptation.py
 
from modeles.comportements.comportement_agressif import ComportementAgressif
from modeles.comportements.comportement_defensif import ComportementDefensif
from modeles.comportements.comportement_berserker import ComportementBerserker
 
def devenir_defensif_si_faible(ennemi):
    """Bascule en mode défensif sous 30% de HP."""
    if ennemi.hp < ennemi.hp_max * 0.3:
        ennemi.set_comportement(ComportementDefensif())
        print(f"  ⚡ {ennemi.nom} change de tactique — il devient Défensif !")
 
 
def devenir_agressif_si_fort(ennemi):
    """Bascule en mode agressif au-dessus de 50% de HP (ennemi soigné)."""
    if ennemi.hp > ennemi.hp_max * 0.5:
        ennemi.set_comportement(ComportementAgressif())
        print(f"  ⚡ {ennemi.nom} change de tactique — il redevient Agressif !")

def devenir_berserker_si_faible(ennemi):
    if ennemi.hp < (ennemi.hp_max * 0.5) and ennemi.hp > (ennemi.hp_max * 0.3) and type(ennemi.get_comportement()) != ComportementBerserker:
        ennemi.set_comportement(ComportementBerserker())
        print(f"  ⚡ {ennemi.nom} change de tactique — il entre en fase berserker !")