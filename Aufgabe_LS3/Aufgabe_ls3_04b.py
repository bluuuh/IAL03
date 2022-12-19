from math import pi


def read_radius():
    radius = float(input("Radius eingeben(m):"))
    return radius


def output(volumen, oberflaeche):
    print(f"Volumen: {volumen}m³\nOberfläche: {oberflaeche}m²")


def calc_volume(radius):
    """Berechene Kugelvolumen mit dem radius

    Args:
        radius (float): radius der Kugel
    """
    volumen = (4/3*pi)*radius**3
    return volumen


def calc_oberflaeche(radius):
    """Berechne Kugeloberfläche mit dem radius

    Args:
        radius (float): radius der Kugel
    """
    oberflaeche = (4*pi)*radius**2
    return oberflaeche


radius = read_radius()
volumen = calc_volume(radius)
oberflaeche = calc_oberflaeche(radius)
output(volumen, oberflaeche)
