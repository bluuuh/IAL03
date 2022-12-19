import benutzerinteraktion as io
import funktionalitaet as calc


def main():
    radius = io.read_radius()
    volumen = calc.calc_volume(radius)
    oberflaeche = calc.calc_oberflaeche(radius)
    io.output(volumen, oberflaeche)


if __name__ == "__main__":
    main()
