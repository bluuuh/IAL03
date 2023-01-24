def auswahl_rechenart():
    """Flag für Rechenart oder Beenden
    Rechenart auswählen
    1 - Grundrechenarten
    2 - Trigonometrie
    Q - Beenden
    """
    print("Rechenart auswählen")
    print("1 - Grundrechenarten")
    print("2 - Trigonometrie")
    print("Q - Beenden")
    eingabe = input().capitalize()
    return eingabe


def wert_einlesen():
    a = input("Zahlenwert eingeben")
    return a


def ergebnis_ausgeben(Ergebnis, *label):
    print(Ergebnis)


print(ergebnis_ausgeben("test"))
