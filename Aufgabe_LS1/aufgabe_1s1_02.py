temperature = input('Enter Temperature:')
temp = temperature.split('°')
if "C" in temperature:
    print(int(temp[0]) * 1.8 + 32)
elif "F" in temperature:
    print((int(temp[0])-32) / 1.8)
else:
    print('falsche Eingabe "zB 70°F"')
