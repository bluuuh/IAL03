""" aufgabe_ls3_03_hauptmodul.py - Modularer Taschenrechner - Hauptmodul
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.12.2020, 20.06.2022
    """


import aufgabe_ls3_03_grundrechenarten as gra
import aufgabe_ls3_03_benutzeroberflaeche as bof
import aufgabe_ls3_03_trigonometrischefunktionen as tf


def taschenrechner_steuerung():
    """ Hauptfunktion des Taschenrechners """
    beenden = False
    while beenden is not True:
        befehl = bof.auswahl_menue()
        if befehl == 1:  # Addition
            zahl1 = bof.zahl_einlesen("Zahl1")
            zahl2 = bof.zahl_einlesen("Zahl2")
            erg = gra.addieren(zahl1, zahl2)
            bof.ergebnis_ausgeben("Addition", erg)
        elif befehl == 2:  # Subtraktion
            zahl1 = bof.zahl_einlesen("Zahl1")
            zahl2 = bof.zahl_einlesen("Zahl2")
            erg = gra.subtrahieren(zahl1, zahl2)
            bof.ergebnis_ausgeben("Subtraktion", erg)
        elif befehl == 3:  # Multiplikation
            zahl1 = bof.zahl_einlesen("Zahl1")
            zahl2 = bof.zahl_einlesen("Zahl2")
            erg = gra.multiplizieren(zahl1, zahl2)
            bof.ergebnis_ausgeben("Multiplikation", erg)
        elif befehl == 4:  # Division
            zahl1 = bof.zahl_einlesen("Zahl1")
            zahl2 = bof.zahl_einlesen("Zahl2")
            erg = gra.dividieren(zahl1, zahl2)
            bof.ergebnis_ausgeben("Division", erg)
        elif befehl == 5:  # Sinus
            zahl = bof.zahl_einlesen("Zahl")
            erg = tf.berechne_sinus(zahl)
            bof.ergebnis_ausgeben("Sinus", erg)
        elif befehl == 6:  # Cosinus
            zahl = bof.zahl_einlesen("Zahl")
            erg = tf.berechne_cosinus(zahl)
            bof.ergebnis_ausgeben("Cosinus", erg)
        elif befehl == 7:  # Tangens
            zahl = bof.zahl_einlesen("Zahl")
            erg = tf.berechne_tangens(zahl)
            bof.ergebnis_ausgeben("Tangens", erg)
        elif befehl == 8:  # Arcus-Sinus
            zahl = bof.zahl_einlesen("Zahl")
            erg = tf.berechne_arcus_sinus(zahl)
            bof.ergebnis_ausgeben("Arcus-Sinus", erg)
        elif befehl == 9:  # Arcus-Cosinus
            zahl = bof.zahl_einlesen("Zahl")
            erg = tf.berechne_arcus_cosinus(zahl)
            bof.ergebnis_ausgeben("Arcus-Cosinus", erg)
        elif befehl == 10:  # Arcus-Tangens
            zahl = bof.zahl_einlesen("Zahl")
            erg = tf.berechne_arcus_tangens(zahl)
            bof.ergebnis_ausgeben("Arcus-Tangens", erg)
        elif befehl == 0:  # Taschenrechner beenden
            beenden = True
        else:
            bof.hinweis_ausgeben("Unbekannter Befehl " + str(befehl))
    bof.hinweis_ausgeben("Taschenrechner beendet")


# Aufruf der Taschenrechnersteuerung
taschenrechner_steuerung()
