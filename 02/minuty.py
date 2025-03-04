# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/parametry-prikazove-radky/parametry/cas-v-minutach

import sys


if len(sys.argv) != 3:
    exit(f"Usage:{sys.argv[0]} <hodiny> <minuty>")


try:
    print(int(sys.argv[1]) * 60 + int(sys.argv[2]))
except ValueError:
    exit("Entered arguments were not digits.")
