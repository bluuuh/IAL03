"""aufgabe_ls3_03_hauptmodul_alt.py - Modularer Taschenrechner - Hauptmodul (Alternativ)
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.12.2020, 20.06.2022
    Es wurde eine alternative Lösung über eine Funktionsliste gewählt.
    Vorteile dieser Lösung:
    + Das Modul Benutzeroberfläche ist unabhägig von den vorhandenen Rechenarten
    + Neue Rechenarten können einfach durch Erweiterung der funktionsliste eingebaut werden
    + Kürzerer Programmcode
    """


import aufgabe_ls3_03_grundrechenarten as gra
import aufgabe_ls3_03_benutzeroberflaeche_alt as bof
import aufgabe_ls3_03_trigonometrischefunktionen as tf


""" Liste der verfügbaren Rechenarten """
funktionsliste = {
    1: {"name": "Addition", "funktion": gra.addieren, "parameter": 2},
    2: {"name": "Subtraktion", "funktion": gra.subtrahieren, "parameter": 2},
    3: {"name": "Multiplikation", "funktion": gra.multiplizieren, "parameter": 2},
    4: {"name": "Division", "funktion": gra.dividieren, "parameter": 2},
    5: {"name": "Sinus", "funktion": tf.berechne_sinus, "parameter": 1},
    6: {"name": "Cosinus", "funktion": tf.berechne_cosinus, "parameter": 1},
    7: {"name": "Tangens", "funktion": tf.berechne_tangens, "parameter": 1},
    8: {"name": "Arcus Sinus", "funktion": tf.berechne_arcus_sinus, "parameter": 1},
    9: {"name": "Arcus Cosinus", "funktion": tf.berechne_arcus_cosinus, "parameter": 1},
    10: {"name": "Arcus Tangens", "funktion": tf.berechne_arcus_tangens, "parameter": 1},
}


def taschenrechnerSteuerung():
    """ Hauptfunktion des Taschenrechners """
    beenden = False
    while beenden != True:
        befehl = bof.auswahl_menue(funktionsliste)
        if befehl in funktionsliste.keys():  # Bekannte Rechenart
            funkBeschreibung = funktionsliste[befehl]
            fkt = funkBeschreibung["funktion"]
            fktName = funkBeschreibung["name"]
            paraAnzahl = funkBeschreibung["parameter"]
            if paraAnzahl == 2:  # Rechenart mit 2 Parametern
                para1 = bof.zahl_einlesen("Zahl 1")
                para2 = bof.zahl_einlesen("Zahl 2")
                erg = fkt(para1, para2)
            elif paraAnzahl == 1:  # Rechenart mit 1 Parametern
                para1 = bof.zahl_einlesen("Zahl 1")
                erg = fkt(para1)
            bof.ergebnis_ausgeben(fktName, erg)
        elif befehl == 0:  # Taschenrechner beenden
            bof.hinweis_ausgeben("Taschenrechner beendet")
            beenden = True
        else:  # Fehlerbehandlung
            bof.hinweis_ausgeben("Unbekannter Befehl " + str(befehl))
    return


# Aufruf der Taschenrechnersteuerung
taschenrechnerSteuerung()
