from math import pi
radius = float(input("Radius eingeben(m):"))


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


volumen = calc_volume(radius)
oberflaeche = calc_oberflaeche(radius)

print(f"Volumen: {volumen}m³\nOberfläche: {oberflaeche}m²")
