"""Modularer Taschenrechner
    Autor: Mike Wagner
    Erstell am: 16.Jan.2023
    geändert am: 16.Jan.2023

    Ein modularer Taschenrechner mit Grundrechenarten und 
    trigonometrischen Funktionen, er besteht aus 4 Modulen

    """

import trigonometrie as trig
import grundfunktionen as basic
import benutzerinteraktion as benutzer


def main():
    while True:
        eingabe = benutzer.auswahl_rechenart()
        if eingabe == "Q":
            quit()
        if eingabe not in "12":
            print("falsche Eingabe")
            continue
        if eingabe == "1":
            a =


if __name__ == "__main__":
    main()
