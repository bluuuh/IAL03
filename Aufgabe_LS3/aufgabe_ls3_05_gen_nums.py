import dblib as db
import random
from time import sleep

verbindung = db.db_verbindung_aufbauen(
    host="localhost", user="root", passwd="Admin", db="ls3_aufgabe5")

for i in range(2000):
    alpha = random.randint(0, 1000)
    beta = random.randint(10, 2000)
    gamma = random.randint(1000, 3000)
    db.db_nicht_abfrage_anweisung(
        verbindung=verbindung, anweisung=f"INSERT INTO sensor_data (alpha, beta, gamma, date) VALUES({alpha}, {beta}, {gamma}, now())")
    sleep(0.1)

print(db.db_abfrage_anweisung(verbindung=verbindung,
      anweisung="SELECT * FROM sensor_data"))
