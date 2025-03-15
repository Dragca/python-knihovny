# Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.
# pro výpočet druhé odmocniny lze použít funkci sqrt z modulu math nebo n ** 0.5

from math import sqrt

while True:
    try:
        cislo = int(input("Vlož číslo: ")) # ošetřit, že jde převod na celé číslo
        break
    except ValueError:
        print('Je třeba zadat celé číslo.')

if cislo < 2:# čísla menší než 2 nejsou prvočísla
    print('Toto není prvočíslo')

else:
    for i in range(2,int(sqrt(cislo))+1):
        if cislo % i == 0:
            print('Zadané číslo není prvočíslo')
            break

    else:
        print('Zadané číslo je prvočíslo')
