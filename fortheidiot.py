"""
    Autor: Felix Werner
    Klasse: FS-ETTZ-22
    Datum: 23.01.2023
    """

U0 = float(input("Geben Sie die Spannung U0 in Volt ein:"))
Ri = float(input("Geben Sie den Innenwiderstand Ri in Ohm ein:"))
RLmax = float(
    input("Geben Sie den maximalen Lastwiderstand RLmax in Ohm ein:"))

print("Sie haben eingegeben:")
print(str(U0)+" V", str(Ri)+" Ω", str(RLmax)+" Ω")


print("_"*20)
RL = 1.0
print("RL", "PL", "Rges",
      "Pges", "I ", "u ")

cols = []
while RL <= round(RLmax):
    rows = []
    Rges = round(RL + Ri, 2)
    I = round(U0 / Rges, 2)
    PL = round(I ** 2 * RL, 2)
    Pges = round(U0 + I, 2)
    u = round(PL / Pges, 2)
    RL += 1.0
    rows.append(RL)
    rows.append(PL)
    rows.append(Rges)
    rows.append(Pges)
    rows.append(I)
    rows.append(u)
    cols.append(rows)
    # print(RL, PL, Rges, Pges, I, u, sep="|")
for i in cols:
    print(i)

print("_"*20)
