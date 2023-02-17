import dblib

db = dblib.db_verbindung_aufbauen(
    host="localhost", user="root", passwd="Admin", db="test")

result = dblib.db_abfrage_anweisung(verbindung=db,
                                    anweisung="SELECT * FROM test_table")
