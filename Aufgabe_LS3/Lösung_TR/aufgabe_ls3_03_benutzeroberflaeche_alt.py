""" aufgabe_ls3_03_benutzeroberflaeche_alt.py - Modularer Taschenrechner - Modul Benutzeroberfläche (alternativ)
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.12.2020, 20.06.2022
    """


def auswahl_menue(funktionsliste):
    """ Auswahlmenü und Benutzerauswahl """
    print("Modularer Taschenrechner")  # Überschrift
    print("------------------------")
    for nummer, wert in funktionsliste.items():  # Befehle auflisten
        print("(" + str(nummer) + ") " + wert["name"])
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
