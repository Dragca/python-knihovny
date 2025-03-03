# h1ttps://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/volby
# kandidáti 1, 2, 3, 4, 5
hlasy = [
    [78774, 43179, 225111, 144799, 242854],
    [91062, 22451, 17475, 53391, 46450],
    [179186, 216499, 4493, 156305, 61222],
    [9619, 53476, 926, 64737, 34566],
    [66904, 85730, 27271, 12964, 38041],
    [118755, 1929, 30426, 25178, 31952],
    [64467, 40993, 81181, 39392, 4335],
    [11221, 97970, 26179, 98539, 112578],
    [171064, 7638, 8752, 96666, 39738],
    [74235, 101680, 18920, 45904, 1922],
    [39309, 1505, 10531, 30458, 40228],
    [131584, 1812, 241122, 22267, 99326],
    [194133, 39985, 200997, 28229, 20780],
    [66188, 51607, 15977, 177272, 17664]
]

nazvy_kraju = [
'Hlavní město Praha', 
'Jihočeský kraj', 
'Jihomoravský kraj', 
'Karlovarský kraj', 
'Kraj Vysočina', 
'Královéhradecký kraj', 
'Liberecký kraj', 
'Moravskoslezský kraj', 
'Olomoucký kraj', 
'Pardubický kraj', 
'Plzeňský kraj', 
'Středočeský kraj', 
'Ústecký kraj', 
'Zlínský kraj']

# 1. Kolik získal každý kandidát hlasů v celé ČR?
# nejdřív jsem si to rozepsala jednotlive, abych to viděla nazorně, k čemu přistupuju, co se mění a jak můžu kod upravit:
# prvni = sum([(kraj[0]) for kraj in hlasy])
# druhy = sum([(kraj[1]) for kraj in hlasy])
# treti = sum([(kraj[2]) for kraj in hlasy])
# ctvrty = sum([(kraj[3]) for kraj in hlasy])
# paty = sum([(kraj[4]) for kraj in hlasy])
# print(prvni, druhy, treti, ctvrty, paty)
# list comprehension a for cyklus  a dostanu v jednom seznamu za sebou všechny hlasy kandidátů
hlasy_kandidatu_celkem = [sum(kraj[i] for kraj in hlasy) for i in range(5)]
print(hlasy_kandidatu_celkem)

#výpis celkových hlasů k jednotlivým kandidátům
for index, hlasy_kandidata in enumerate(hlasy_kandidatu_celkem, start=1):
    print(f"kandidát {index}: {hlasy_kandidata} hlasů")

# 2.Který kandidát vyhrál první kolo voleb?
index_nejvíc_hlasu = hlasy_kandidatu_celkem.index(max(hlasy_kandidatu_celkem))

print(f"Nejvíce hlasů obdržel kandidát číslo {index_nejvíc_hlasu + 1}.")

# 3. Ve kterých krajích byla nejvyšší a nejnižší volební účast

hlasy_kraje = [sum(kraj) for kraj in hlasy]# dostanu seznam s počtem hlasů v každém kraji

index_max = (hlasy_kraje.index(max(hlasy_kraje)))
index_min = (hlasy_kraje.index(min(hlasy_kraje)))

print(f"Nejvyšší volbení účast byla v {nazvy_kraju[index_max]} a nejnižší volební účast byla v {nazvy_kraju[index_min]}.")

# 4.Vytvořte tabulku, která ukazuje který kandidát vyhrál v kterém kraji.
vitez_kraje = [kraj.index(max(kraj)) + 1 for kraj in hlasy]
print(vitez_kraje)

kraj_vitez = list(zip(nazvy_kraju, vitez_kraje))
print(kraj_vitez)

for kraj, vitez in zip(nazvy_kraju, vitez_kraje):
    print(f"V {kraj} vyhrál kandidát číslo {vitez}.")

# 5. Vytvořte tabulku podobnou té z tohoto cvičení, která místo čísel bude obsahovat jaké procento celkového počtu hlasů získal každý kandidát v daném kraji.
# hlasy kandidata/ celkové hlasy v kraji
volby_procenta = []

for kraj in hlasy:
    for kandidat in kraj:
        vysledek = kandidat/sum(kraj)
        na_procenta = vysledek * 100
        zaokrouhlit_na_setiny = round(na_procenta, 2)
        volby_procenta.append(zaokrouhlit_na_setiny)
print(volby_procenta)

# volby elegantně 
print([[round((kandidat/sum(kraj)) * 100, 2) for kandidat in kraj] for kraj in hlasy])