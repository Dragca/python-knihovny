# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
    return [f"{x // 60}:{x % 60:0>2}" for x in vstup]

