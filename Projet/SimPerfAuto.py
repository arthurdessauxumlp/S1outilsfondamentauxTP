
import math

# CONSTANTES PHYSIQUES
G = 9.81              # Accélération de la pesanteur (m/s^2)
RHO_AIR = 1.225       # Masse volumique de l'air (kg/m^3)
CR = 0.012            # Coefficient de résistance au roulement

class Vehicule:
    def __init__(self, nom, masse, cx, surface, empattement, h_cg):
        self.nom = nom
        self.masse = masse
        self.cx = cx
        self.surface = surface
        self.L = empattement
        self.h = h_cg

def calculer_charges_essieux(vehicule, deceleration):
    m, L, h = vehicule.masse, vehicule.L, vehicule.h
    f_z_avant = (m * G * (L / 2) + m * deceleration * h) / L
    f_z_arriere = (m * G * (L / 2) - m * deceleration * h) / L
    return max(0.0, f_z_avant), max(0.0, f_z_arriere)

# =====================================================================
# INTÉGRATION EULER CORRIGÉE (Pas exacts sans erreur de flottants)
# =====================================================================
def vitesse_a_l_instant(t, vehicule, v_initiale_ms, dt=0.01):
    vitesse = v_initiale_ms
    n_pas = int(round(t / dt))  # Nombre exact d'itérations
    
    for _ in range(n_pas):
        if vitesse <= 0:
            return 0.0
        
        force_aero = 0.5 * RHO_AIR * vehicule.cx * vehicule.surface * (vitesse ** 2)
        force_roulement = CR * vehicule.masse * G
        force_freinage = 0.8 * vehicule.masse * G  # Adhérence mu = 0.8
        
        force_totale = force_freinage + force_aero + force_roulement
        deceleration = force_totale / vehicule.masse

        vitesse -= deceleration * dt

    return max(0.0, vitesse)

# =====================================================================
# DICHOTOMIE CORRIGÉE (Recherche du vrai zéro)
# =====================================================================
def trouver_temps_arret_dichotomie(vehicule, v_initiale_ms, dt=0.01, tol=1e-4, max_iter=100):
    a, b = 0.0, 10.0  # Borne [0s, 10s]
    iterations = 0

    while (b - a) / 2.0 > tol and iterations < max_iter:
        m = (a + b) / 2.0
        v_m = vitesse_a_l_instant(m, vehicule, v_initiale_ms, dt=dt)

        if v_m <= 0:
            b = m  # Si la voiture est déjà arrêtée à m, l'arrêt est plus tôt
        else:
            a = m  # Si elle roule encore, l'arrêt est plus tard
        iterations += 1

    return (a + b) / 2.0, iterations

# =====================================================================
# ÉTUDE DU PAS DE TEMPS (dt)
# =====================================================================
def etude_sensibilite_dt(vehicule, v_initiale_ms):
    pasi = [0.2, 0.05, 0.01, 0.001, 0.0001]
    print("\n" + "="*60)
    print(" ANALYSE NUMÉRIQUE : ÉTUDE DU PAS DE TEMPS (dt) ")
    print("="*60)
    print(f"{'dt (s)':<10} | {'t_arrêt (s)':<15} | {'Vitesse à t=3s (m/s)':<25}")
    print("-" * 60)

    for dt in pasi:
        t_arr, _ = trouver_temps_arret_dichotomie(vehicule, v_initiale_ms, dt=dt)
        v_test = vitesse_a_l_instant(3.0, vehicule, v_initiale_ms, dt=dt)
        print(f"{dt:<10} | {t_arr:<15.5f} | {v_test:<25.8f}")

def saisir_float(prompt, defaut):
    valeur = input(f"{prompt} [Par défaut: {defaut}] : ").strip()
    if not valeur:
        return defaut
    return float(valeur)

def menu_saisie():
    print("="*60)
    print(" OUTIL D'ANALYSE DE FREINAGE & SIMULATEUR NUMÉRIQUE ")
    print("="*60)

    nom = input("Nom/Modèle du véhicule [Ex: Sportive] : ").strip() or "Sportive"
    masse = saisir_float("Masse (kg)", 1400.0)
    v_kmh = saisir_float("Vitesse initiale (km/h)", 130.0)
    cx = saisir_float("Coefficient Cx", 0.32)
    surface = saisir_float("Surface frontale (m²)", 2.1)
    L = saisir_float("Empattement (m)", 2.7)
    h = saisir_float("Hauteur centre de gravité (m)", 0.55)

    auto = Vehicule(nom, masse, cx, surface, L, h)
    v_init_ms = v_kmh / 3.6

    print("\n" + ">"*10 + f" LANCEMENT DES CALCULS POUR : {auto.nom} " + "<"*10)
    
    t_exact, n_iter = trouver_temps_arret_dichotomie(auto, v_init_ms, dt=0.01)
    print(f"\n[TP3] Temps d'arrêt exact (Dichotomie) : {t_exact:.4f} s en {n_iter} itérations.")

    a_moy = v_init_ms / t_exact
    f_av, f_arr = calculer_charges_essieux(auto, a_moy)
    print(f"\n[TP4] Transfert de charge à décélération moyenne ({a_moy:.2f} m/s²) :")
    print(f" - Essieu AVANT   : {f_av:.1f} N")
    print(f" - Essieu ARRIÈRE : {f_arr:.1f} N")

    etude_sensibilite_dt(auto, v_init_ms)

if __name__ == "__main__":
    menu_saisie()
