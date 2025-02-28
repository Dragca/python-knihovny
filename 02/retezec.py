# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/parametry-prikazove-radky/parametry/uprava-retezce

import sys

if len(sys.argv) != 2:
    exit(f"Usage:{sys.argv[0]} <retezec>")


print(sys.argv[1].replace(' ', '_'))
