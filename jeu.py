from entites.ennemi_agressif import EnnemiAgressif
from entites.ennemi_aleatoire import EnnemiAleatoire
from entites.ennemi_defensif import EnnemiDefensif
from entites.ennemi_furtif import EnnemiFurtif

class Jeu:
    def __init__(self):
        self.heros_hp = 100
        self.heros_hp_max = 100
        self.heros_attaque = 20

        self.ennemis = [
            EnnemiAgressif("Goblin", 50, 10),
            EnnemiDefensif("Dragon", 100, 20),
            EnnemiFurtif("Voleur", 30, 15),
        ]

    def ennemis_vivants(self):
        return [e for e in self.ennemis if e.est_vivant()]

    def demarrer(self):
        print("\n===========================================")
        print("        LE DONJON DES ALGORITHMES")
        print("===========================================\n")

        tour = 1

        while self.heros_hp > 0 and self.ennemis_vivants():
            # Afficher l'état
            print(f"Tour {tour} — Héros (HP: {self.heros_hp}/{self.heros_hp_max})")
            print("\nEnnemis :")
            vivants = self.ennemis_vivants()
            for i, ennemi in enumerate(vivants, 1):
                print(f"  [{i}] {ennemi.nom} (HP: {ennemi.hp}/{ennemi.hp_max}) — {type(ennemi).__name__}")
            print()

            # Demander l'action du héros
            while True:
                action = input("Votre action ? (a)ttaquer / (d)éfendre : ").strip().lower()
                if action in ["a", "d"]:
                    break
                print("Choix invalide.")
            action_heros = "attaque" if action == "a" else "defend"

            # Demander la cible si attaque
            cible = None
            if action_heros == "attaque":
                if len(vivants) == 1:
                    cible = vivants[0]
                else:
                    while True:
                        try:
                            choix = int(input(f"Quel ennemi ? (1-{len(vivants)}) : "))
                            if 1 <= choix <= len(vivants):
                                cible = vivants[choix - 1]
                                break
                        except ValueError:
                            pass
                        print("Choix invalide.")

            # Chaque ennemi décide de son action
            actions_ennemis = {e: e.agir() for e in vivants}

            print("--- Résultats ---")

            # Résoudre l'attaque du héros
            if action_heros == "attaque" and cible:
                if actions_ennemis.get(cible) == "defend":
                    degats = self.heros_attaque // 2
                    print(f"Vous attaquez {cible.nom} — il se défend ! Seulement {degats} dégâts infligés.")
                else:
                    degats = self.heros_attaque
                    print(f"Vous attaquez {cible.nom} pour {degats} dégâts !")
                cible.recevoir_degats(degats)

            # Résoudre les actions des ennemis
            for ennemi, action_ennemi in actions_ennemis.items():
                if not ennemi.est_vivant():
                    continue
                if action_ennemi == "attaque":
                    if action_heros == "defend":
                        degats = ennemi.attaque // 2
                        print(f"  → {ennemi.nom} attaque — vous vous défendez ! Seulement {degats} dégâts reçus.")
                    else:
                        degats = ennemi.attaque
                        print(f"  → {ennemi.nom} vous attaque pour {degats} dégâts !")
                    self.heros_hp = max(0, self.heros_hp - degats)
                else:
                    print(f"  → {ennemi.nom} se défend.")

            # Adaptation des comportements
            for ennemi in self.ennemis_vivants():
                if ennemi.hp < ennemi.hp_max * 0.3 and type(ennemi).__name__ != "EnnemiDefensif":
                    


                    
                    print(f"  ⚡ {ennemi.nom} change de tactique — il devient Défensif !")

            print()
            tour += 1

        if self.heros_hp > 0:
            print("\n===========================================")
            print("  🏆 VICTOIRE ! Tous les ennemis sont vaincus !")
            print("===========================================\n")
        else:
            print("\n===========================================")
            print("  💀 DÉFAITE ! Le héros est tombé...")
            print("===========================================\n")
