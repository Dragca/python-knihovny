# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
    trvani = [prevod_na_retezec(x) for x in vstup]
    return trvani


def prevod_na_retezec(stopaz):
    hodin = stopaz // 60
    minut = stopaz % 60
    return f"{hodin}:{minut:0>2}"


# print(prevod((136, 105, 82)))
