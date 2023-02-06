""" aufgabe_ls3_03_trigonometrischefunktionen.py - Modularer Taschenrechner - Modul trigonometrische Funktionen
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  05.12.2020, 20.06.2022
    """


import math


def berechne_sinus(zahl):
    """Sinus-Funktion"""
    ergebnis = math.sin(zahl)
    return ergebnis


def berechne_cosinus(zahl):
    """Cosinus-Funktion"""
    ergebnis = math.cos(zahl)
    return ergebnis


def berechne_tangens(zahl):
    """Tangens-Funktion"""
    ergebnis = math.tan(zahl)
    return ergebnis


def berechne_arcus_sinus(zahl):
    """Arcus-Sinus-Funktion"""
    ergebnis = math.asin(zahl)
    return ergebnis


def berechne_arcus_cosinus(zahl):
    """Arcus-Cosinus-Funktion"""
    ergebnis = math.acos(zahl)
    return ergebnis


def berechne_arcus_tangens(zahl):
    """Arcus-Tangens-Funktion"""
    ergebnis = math.atan(zahl)
    return ergebnis
