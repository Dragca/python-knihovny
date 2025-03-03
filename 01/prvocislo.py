# Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.

try:
    cislo = int(input("Vlož číslo: "))
# delitelne = []# nejdriv jsem si to musela rozepsat takto 
# for i in range(1,cislo + 1):
#     if cislo % i == 0:
#         delitelne.append(i)
# upraveno pomocí list comprehension
    delitelne = [i for i in range(1, cislo + 1)if cislo % i == 0]
    if len(delitelne) == 2:
        print('zadané číslo je prvočíslo')
    else:
        print('zadané číslo není prvočíslo')

except ValueError:
    print('Je třeba zadat celé číslo.')
