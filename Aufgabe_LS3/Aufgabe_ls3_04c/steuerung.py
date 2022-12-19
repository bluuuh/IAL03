"""
Kugelberechnungen
Autor, Klases : Mike Wagner, FS-ETTZ-22
Erstelldatum : 19.12.2022
    """

import benutzerinteraktion as io
import funktionalitaet as calc


def main():
    radius = io.read_radius()
    volumen = calc.volume(radius)
    oberflaeche = calc.oberflaeche(radius)
    io.output(volumen, oberflaeche)


if __name__ == "__main__":
    while True:
        main()
