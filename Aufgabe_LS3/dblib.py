import mysql.connector


def db_verbindung_aufbauen(host, user, passwd, db):
    """Funktion zum Verbindungsaufbau mit einer MySQL-Datenbank"""
    verbindung = mysql.connector.connect(
        host=host, port=49153, user=user, passwd=passwd, db=db
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
