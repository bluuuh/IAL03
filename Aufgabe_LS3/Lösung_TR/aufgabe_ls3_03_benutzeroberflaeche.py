"""aufgabe_ls3_03_benutzeroberflaeche.py - Modularer Taschenrechner - Modul Benutzeroberfläche
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.12.2020, 20.06.2022
    """


def auswahl_menue():
    """ Auswahlmenü und Benutzerauswahl """
    print("Modularer Taschenrechner")  # Überschrift
    print("------------------------")
    print("(1) Addition")  # Auswahlmenü
    print("(2) Subtraktion")
    print("(3) Multiplikation")
    print("(4) Division")
    print("(5) Sinus")
    print("(6) Cosinus")
    print("(7) Tangens")
    print("(8) Arcus Sinus")
    print("(9) Arcus Cosinus")
    print("(10) Arcus Tangens")
    print("(0) Beenden")
    befehl = int(input("Auswahl: "))  # Benutzerauswahl
    print("")
    return befehl


def zahl_einlesen(label):
    """ Funktion zum Einlesen einer Zahl """
    zahl = float(input(label + ": "))
    return zahl


def ergebnis_ausgeben(rechenart, ergebnis):
    """ Funktion zum Ausgeben des Ergebnises """
    print("Das Ergebnis der", rechenart, "lautet", ergebnis)
    print("")


def hinweis_ausgeben(hinweis_text):
    """ Funktion zum Ausgeben eines Hinweistextes """
    print(hinweis_text)
    print("")
