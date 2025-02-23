# Napiš funkci, která vrátí ze iterovatelného vstupu množinu zaokrouhlených hodnot

# def mnozina_zaokrouhlenych(vstup):
#     mnozina = set()
#     for prvek in vstup:
#         mnozina.add(round(prvek))

#     return mnozina

def mnozina_zaokrouhlenych(vstup):
    return {round(prvek) for prvek in vstup}
