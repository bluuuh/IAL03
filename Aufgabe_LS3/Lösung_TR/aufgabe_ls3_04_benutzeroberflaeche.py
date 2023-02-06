"""aufgabe_ls3_04_benutzeroberflaeche.py - Temperaturabhängiger Widerstandsrechner - Benutzeroberfläche
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  30.06.2022
    """


def auswahl_menue():
    """Auswahlmenü und Benutzerauswahl"""
    print("Temperaturabhängiger Widerstandsrechner")  # Überschrift
    print("---------------------------------------")
    print("(1) Material, Temperatur und R20 sind bekannt.")  # Auswahlmenü
    print("(2) Material, Temperatur, Länge und Querschnitt sind bekannt.")
    print("(0) Beenden")
    befehl = int(input("Auswahl: "))  # Benutzerauswahl
    print("")
    return befehl


def material_eingeben():
    """Material einlesen"""
    material = 0
    while material < 1 or material > 4:
        print("Material:   ")
        print("(1) - Silber")
        print("(2) - Kupfer")
        print("(3) - Gold")
        print("(4) - Aluminium")
        material = int(input("Material:   "))
        if material < 1 or material > 4:
            hinweis_ausgeben("Unbekanntes Material")
    return material


def untermenue_1():
    """Untermenü 1"""
    material = material_eingeben()
    temp = float(input("Temperatur (°C): "))
    r_20 = float(input("R20 (Ohm): "))
    return material, temp, r_20


def untermenue_2():
    """Untermenü 2"""
    material = material_eingeben()
    temp = float(input("Temperatur (°C): "))
    laenge = float(input("Länge (m): "))
    querschnitt = float(input("Querschnitt (mm2): "))
    return material, temp, laenge, querschnitt


def zahl_einlesen(label):
    """Funktion zum Einlesen einer Zahl"""
    zahl = float(input(label + ": "))
    return zahl


def ergebnis_ausgeben(text, ergebnis):
    """Funktion zum Ausgeben des Ergebnises"""
    ergebnis = round( ergebnis, 2)
    ausgabe_text = text + ": " + str(ergebnis)
    print(ausgabe_text)
    print("")


def hinweis_ausgeben(hinweis_text):
    """Funktion zum Ausgeben eines Hinweistextes"""
    print(hinweis_text)
    print("")
