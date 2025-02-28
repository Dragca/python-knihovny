# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/parametry-prikazove-radky/parametry/cas-v-minutach

import sys
                                                            # ošetřeno potřebné množství zadaných parametrů
                                                            # v rámci opakování ošetřeno blokem try/except že jdou parametry převést na int
if len(sys.argv) != 3:
    exit(f"Usage:{sys.argv[0]} <hodiny> <minuty>")


try:
    print(int(sys.argv[1]) * 60 + int(sys.argv[2]))
except ValueError:
    exit("Entered arguments were not digits.")


# v rámci procvičení jsem si to napsala ještě ve funkci
def convert(h, m):
    """converts the value in hours and minutes and return total number of minutes"""
    return int(h) * 60 + int(m)

try:
    print(convert(sys.argv[1], sys.argv[2]))
except ValueError:
    print('Vložený argument nebylo číslo')
    sys.exit(1)