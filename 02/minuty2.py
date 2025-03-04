# v rámci procvičení jsem si ukol převod na minuty napsala ještě ve funkci
# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/parametry-prikazove-radky/parametry/cas-v-minutach

import sys


if len(sys.argv) != 3:
    exit(f"Usage:{sys.argv[0]} <hodiny> <minuty>")

def convert(h, m):
    """converts the value in hours and minutes and return total number of minutes"""
    return int(h) * 60 + int(m)

try:
    print(convert(sys.argv[1], sys.argv[2]))
except ValueError:
    print('Vložený argument nebylo číslo')
