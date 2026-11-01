import math
import tkinter as tk
from tkinter import ttk, messagebox


# CONSTANTES PHYSIQUES ET DE CALIBRATION

RHO_AIR = 1.225
G = 9.81
CR = 0.012

COEFF_CALIBRATION_ACCEL = 1.10
TEMPS_CHANGEMENT_RAPPORT = 0.4

RENDEMENT_VMAX = 0.85
COEFF_VMAX = 0.95
MARGE_ERREUR = 10



# FONCTIONS DE CALCUL PHYSIQUE

def ch_vers_watts(ch):
    return ch * 735.5


def kmh_vers_ms(v):
    return v / 3.6


def ms_vers_kmh(v):
    return v * 3.6


def coeff_transmission(transmission):
    coeffs = {"Traction": 0.95, "Propulsion": 1.00, "4x4": 1.05}
    return coeffs.get(transmission, 1.0)


def force_aerodynamique(vitesse_ms, cx, surface):
    return 0.5 * RHO_AIR * cx * surface * (vitesse_ms ** 2)


def force_roulement(masse):
    return CR * masse * G


def puissance_effective(puissance_max, vitesse_kmh):
    facteur = 1 - math.exp(-vitesse_kmh / 50)
    return puissance_max * facteur


def coeff_roue(diametre):
    diametre_reference = 0.65
    return diametre_reference / diametre


def simuler_accelerations(masse, puissance_ch, cx, surface, transmission, diametre, v_debut, v_fin):
    """Calcule les paliers d'accélération, la plage personnalisée (v_debut -> v_fin) et l'historique."""
    puissance_max = ch_vers_watts(puissance_ch)
    coeff_trans = coeff_transmission(transmission)
    coeff_diam = coeff_roue(diametre)

    # S'assurer que les vitesses cible incluent les paliers et la plage personnalisée
    paliers = sorted(list(set([50, 80, 100, 130, v_debut, v_fin])))
    temps_paliers = {}
    courbe = [(0.0, 0.0)]

    vitesse = 0.5  # m/s
    temps = 0.0
    dt = 0.05
    next_sample = 0.05

    t_debut_val = None
    t_fin_val = None
    v_debut_ms = kmh_vers_ms(v_debut)
    v_fin_ms = kmh_vers_ms(v_fin)

    while temps <= 120:
        vitesse_kmh = ms_vers_kmh(vitesse)

        # Enregistrement des paliers
        for p in list(paliers):
            if vitesse_kmh >= p and p not in temps_paliers:
                t_final = (temps + TEMPS_CHANGEMENT_RAPPORT) * COEFF_CALIBRATION_ACCEL
                temps_paliers[p] = round(t_final, 2)

        # Capture précise pour la plage personnalisée
        if t_debut_val is None and vitesse >= v_debut_ms:
            t_debut_val = temps
        if t_fin_val is None and vitesse >= v_fin_ms:
            t_fin_val = temps

        puissance = puissance_effective(puissance_max, vitesse_kmh)
        force_motrice = (puissance / vitesse) * coeff_trans * coeff_diam

        resistance_air = force_aerodynamique(vitesse, cx, surface)
        resistance_roulement = force_roulement(masse)

        force_totale = force_motrice - resistance_air - resistance_roulement
        acceleration = force_totale / masse

        if acceleration <= 0:
            break

        vitesse += acceleration * dt
        temps += dt

        if temps >= next_sample:
            courbe.append((temps, vitesse_kmh))
            next_sample += 0.05

    # Calcul du temps pour une plage d'acceleration personnalisée (v_debut -> v_fin)
    temps_personnalise = None
    if v_debut == v_fin:
        temps_personnalise = 0.0
    elif t_fin_val is not None:
        if v_debut == 0 or t_debut_val is not None:
            start_t = t_debut_val if v_debut > 0 else 0.0
            if t_fin_val >= start_t:
                temps_personnalise = round((t_fin_val - start_t) * COEFF_CALIBRATION_ACCEL, 2)

    return temps_paliers, courbe, temps_personnalise


def vitesse_max(puissance_ch, cx, surface):
    puissance = ch_vers_watts(puissance_ch) * RENDEMENT_VMAX
    vmax = ((2 * puissance) / (RHO_AIR * cx * surface)) ** (1 / 3)
    vmax *= COEFF_VMAX
    return round(ms_vers_kmh(vmax))


def intervalle(valeur):
    mini = valeur * (1 - MARGE_ERREUR / 100)
    maxi = valeur * (1 + MARGE_ERREUR / 100)
    return mini, maxi


# APPLICATION GRAPHIQUE AVEC PLAGE PERSONNALISÉE
class SimulateurApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de Performances Automobiles - Plage Personnalisée")
        self.geometry("940x680")
        self.minsize(840, 600)

        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")

        self.creer_widgets()

    def creer_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        gauche_frame = ttk.Frame(self, padding=12)
        gauche_frame.grid(row=0, column=0, sticky="nsew")

        droite_frame = ttk.Frame(self, padding=12)
        droite_frame.grid(row=0, column=1, sticky="nsew")
        droite_frame.rowconfigure(1, weight=1)
        droite_frame.columnconfigure(0, weight=1)

        # --- SECTION GAUCHE : FORMULAIRE ---
        cadre_saisie = ttk.LabelFrame(gauche_frame, text=" Paramètres du Véhicule ", padding=10)
        cadre_saisie.pack(fill="x", pady=(0, 10))

        champs_config = [
            ("Masse (kg) :", "masse", "1380"),
            ("Puissance (ch) :", "puissance", "250"),
            ("Cx :", "cx", "0.34"),
            ("Surface (m²) :", "surface", "2.15"),
            ("Diamètre roue (m) :", "diametre", "0.65"),
            ("Vitesse Début (km/h) :", "v_debut", "80"),
            ("Vitesse Fin (km/h) :", "v_fin", "120")
        ]

        self.entrees = {}
        for idx, (label_txt, cle, defaut) in enumerate(champs_config):
            ttk.Label(cadre_saisie, text=label_txt).grid(row=idx, column=0, sticky="w", pady=3)
            entree = ttk.Entry(cadre_saisie, width=12, justify="right")
            entree.grid(row=idx, column=1, sticky="e", pady=3, padx=5)
            entree.insert(0, defaut)
            self.entrees[cle] = entree

        ttk.Label(cadre_saisie, text="Transmission :").grid(row=len(champs_config), column=0, sticky="w", pady=3)
        self.choix_transmission = ttk.Combobox(cadre_saisie, values=["Traction", "Propulsion", "4x4"], state="readonly", width=11)
        self.choix_transmission.current(0)
        self.choix_transmission.grid(row=len(champs_config), column=1, sticky="e", pady=3, padx=5)

        btn_calculer = ttk.Button(gauche_frame, text="Lancer la Simulation", command=self.lancer_calcul)
        btn_calculer.pack(fill="x", pady=8, ipady=4)

        # --- SECTION GAUCHE : RÉSULTATS TEXTUELS ---
        cadre_resultat = ttk.LabelFrame(gauche_frame, text=" Résultats de l'Analyse ", padding=10)
        cadre_resultat.pack(fill="both", expand=True, pady=(5, 0))

        self.label_resultat = ttk.Label(
            cadre_resultat,
            text="Renseignez les paramètres\net lancez la simulation.",
            font=("Consolas", 9),
            anchor="nw",
            justify="left"
        )
        self.label_resultat.pack(fill="both", expand=True)

        # --- SECTION DROITE : GRAPHIQUE CANVAS ---
        ttk.Label(droite_frame, text="Courbe de Vitesse (km/h) en fonction du Temps (s)", font=("Helvetica", 11, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))

        self.canvas = tk.Canvas(droite_frame, bg="white", highlightthickness=1, highlightbackground="#cccccc")
        self.canvas.grid(row=1, column=0, sticky="nsew")
        self.canvas.bind("<Configure>", lambda e: self.redessiner_graphique())

        self.derniere_courbe = None

    def lancer_calcul(self):
        try:
            masse = float(self.entrees["masse"].get())
            puissance = float(self.entrees["puissance"].get())
            cx = float(self.entrees["cx"].get())
            surface = float(self.entrees["surface"].get())
            diametre = float(self.entrees["diametre"].get())
            v_debut = float(self.entrees["v_debut"].get())
            v_fin = float(self.entrees["v_fin"].get())
            transmission = self.choix_transmission.get()

            if masse <= 0 or puissance <= 0 or diametre <= 0 or cx <= 0 or surface <= 0:
                messagebox.showwarning("Valeurs invalides", "Les caractéristiques techniques doivent être supérieures à zéro.")
                return
            if v_debut < 0 or v_fin < 0 or v_debut > v_fin:
                messagebox.showwarning("Plage invalide", "La vitesse de début doit être positive et inférieure ou égale à la vitesse de fin.")
                return

            rapport = masse / puissance
            circonference = math.pi * diametre
            paliers, courbe, t_perso = simuler_accelerations(masse, puissance, cx, surface, transmission, diametre, v_debut, v_fin)
            vmax = vitesse_max(puissance, cx, surface)

            t100 = paliers.get(100)
            if t100:
                t100_min, t100_max = intervalle(t100)
                txt_t100_probable = f"{t100_min:.2f}s à {t100_max:.2f}s"
            else:
                txt_t100_probable = "Non atteint"

            vmax_min, vmax_max = intervalle(vmax)

            def fmt(val):
                return f"{val:.2f} s" if val is not None else "Non atteint"

            txt_perso_formatted = f"{t_perso:.2f} s" if t_perso is not None else "Non atteint"

            texte = (
                f"• Poids/Puissance : {rapport:.2f} kg/ch\n"
                f"• Circonférence   : {circonference:.2f} m\n"
                f"-----------------------------\n"
                f"• 0-50 km/h   : {fmt(paliers.get(50))}\n"
                f"• 0-80 km/h   : {fmt(paliers.get(80))}\n"
                f"• 0-100 km/h : {fmt(paliers.get(100))}\n"
                f"• 0-130 km/h : {fmt(paliers.get(130))}\n"
                f"-----------------------------\n"
                f"• De {int(v_debut)} à {int(v_fin)} km/h : {txt_perso_formatted}\n"
                f"-----------------------------\n"
                f"• 0-100 (prob.) : {txt_t100_probable}\n"
                f"• Vmax estimée  : {vmax} km/h\n"
                f"  (Plage : {vmax_min:.0f}-{vmax_max:.0f})"
            )

            self.label_resultat.config(text=texte)
            self.derniere_courbe = courbe
            self.redessiner_graphique()

        except ValueError:
            messagebox.showerror("Erreur de Saisie", "Veuillez entrer des nombres valides dans tous les champs.")

    def redessiner_graphique(self):
        c = self.canvas
        c.delete("all")
        if not self.derniere_courbe:
            return

        w = c.winfo_width()
        h = c.winfo_height()
        if w < 50 or h < 50:
            return

        ml, mr, mt, mb = 45, 15, 20, 35
        pw = w - ml - mr
        ph = h - mt - mb

        pts = self.derniere_courbe
        t_max = max(pts[-1][0], 1)
        v_max = max([v for _, v in pts] + [100])
        v_max_axe = math.ceil(v_max * 1.1 / 20) * 20

        X = lambda t: ml + pw * (t / t_max)
        Y = lambda v: mt + ph * (1 - v / v_max_axe)

        # Grille et axes Y (Vitesse)
        steps_v = 5 if v_max_axe <= 100 else 10
        for v in range(0, int(v_max_axe) + 1, steps_v * 10):
            y_pos = Y(v)
            c.create_line(ml, y_pos, w - mr, y_pos, fill="#eeeeee")
            c.create_text(ml - 5, y_pos, text=str(v), anchor="e", font=("Arial", 8), fill="#666666")

        # Grille et axes X (Temps)
        t_pas = 2 if t_max <= 10 else 5 if t_max <= 25 else 10
        t = 0
        while t <= t_max:
            x_pos = X(t)
            c.create_line(x_pos, mt, x_pos, h - mb, fill="#f5f5f5")
            c.create_text(x_pos, h - mb + 12, text=str(int(t)), font=("Arial", 8), fill="#666666")
            t += t_pas

        c.create_line(ml, mt, ml, h - mb, fill="#444444", width=1.5)
        c.create_line(ml, h - mb, w - mr, h - mb, fill="#444444", width=1.5)

        coords = []
        for t, v in pts:
            coords.extend((X(t), Y(v)))

        if len(coords) >= 4:
            c.create_line(coords, fill="#1f6feb", width=2.5, smooth=False)

        if 100 <= v_max_axe:
            y_100 = Y(100)
            c.create_line(ml, y_100, w - mr, y_100, fill="#d29922", dash=(4, 3))
            c.create_text(w - mr - 2, y_100 - 8, text="100 km/h", anchor="e", font=("Arial", 8), fill="#d29922")


if __name__ == "__main__":
    app = SimulateurApp()
    app.mainloop()
