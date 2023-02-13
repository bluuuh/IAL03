"""Aufgabe_ls3_00 - Ausgangsprogramm - Zusammenspiel von Python mit MySQL
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  14.04.2020, 20.06.2022
    """

from random import random
import mysql.connector


def db_verbindung_aufbauen(host, user, passwd, db):
    """Funktion zum Verbindungsaufbau mit einer MySQL-Datenbank"""
    verbindung = mysql.connector.connect(
        host=host, port=3306, user=user, passwd=passwd, db=db
    )
    return verbindung


def db_verbindung_abbauen(verbindung):
    """Funktion zum Verbindungsabbau bei einer MySQL-Datenbank"""
    verbindung.close()


def db_nicht_abfrage_anweisung(verbindung, anweisung):
    """Funktion zur Ausführung einer Nicht-Abfrage-Anweisung bei MySQL-Datenbank"""
    cursor = verbindung.cursor()
    cursor.execute(anweisung)
    verbindung.commit()
    cursor.close()


def db_abfrage_anweisung(verbindung, anweisung):
    """Funktion zur Ausführung einer Nicht-Abfrage-Anweisung bei MySQL-Datenbank"""
    cursor = verbindung.cursor()
    cursor.execute(anweisung)
    ergebnis_menge = cursor.fetchall()
    cursor.close()
    return ergebnis_menge


def db_zugriffswerte():
    """Funktion, die die Zugriffsdaten für eine MySQL-Datenbank liefert"""
    return "localhost", "root", "", "aufgabe_ls3_01"


# Skript ###################################################################

# Verbindung zur Datenbank aufbauen
print("Verbindung zur Datenbank aufbauen")
print("")
host, user, passwd, db = db_zugriffswerte()
connection = db_verbindung_aufbauen(host, user, passwd, db)

# 50 Werte in Datenbank schreiben
print("50 Werte in Datenbank schreiben")
i = 1
while i <= 50:
    wert = random() * 100
    wert = round(wert, 2)
    sql_anweisung = "INSERT INTO t1_demo ( t1_wert) VALUES ( " + \
        str(wert) + ")"
    db_nicht_abfrage_anweisung(connection, sql_anweisung)
    i = i + 1
print("")

# Tabelleninhalt ausgeben
print("Tabelleninhalt ausgeben:")
print("------------------------")
print("")
print(" Nr : Zeitpunkt : Wert")
ergebnis_menge = db_abfrage_anweisung(connection, "SELECT * FROM t1_demo")
for zeile in ergebnis_menge:  # Ergebnis zeilenweise durchlaufen und ausgeben
    print(str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]))

print("")

# Verbindung zur Datenbank abbauen
print("Verbindung zur Datenbank abbauen")
print("")
db_verbindung_abbauen(connection)
