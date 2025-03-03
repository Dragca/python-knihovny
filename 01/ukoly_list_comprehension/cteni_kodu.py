# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/cteni-kodu

seznam = [1, 4, 9, 16, 25, 36, 49, 64]
print([x**0.5 for x in seznam])# každý prvek seznamu umocní 0,5 a vrátí výsledky v seznamu
print([x % 2 for x in seznam])# pro každý prvek seznamu vrátí zbytek po celočíselném dělení dvěmi a výsledky budou v seznamu
print([[x // 2, x % 2] for x in seznam])# vrací seznam seznamů, kde v každém podseznamu bude výsledek celočíselného dělení dvěma a zbytek po tomto dělení

seznam = ['12.03.2014', '10.01.2015', '06.06.1986']
print([int(datum[3:5]) for datum in seznam])# vezme z každého řetězce v seznamu 4.a 5. znak a převede jej na int, výsledky vrací v seznamu  
print([int(datum[:2])-1 for datum in seznam])# vezme první dva znaky z každého řetězce seznamu, převede je na celé číslo a odečte od něj jedničku, výsledky vrací v seznamu
print([[int(datum[:2]), int(datum[3:5]), int(datum[6:])] for datum in seznam])# vezme z každého řetězce seznamu zadané znaky, převede je na celé číslo a z každého řetězce vrátí seznam čísel [dd, mm, rrrr] a ty jsou jednotlivé podseznamy seznamu
print([datum.split('.') for datum in seznam])# rozdělí každý řetězec seznamu podle oddělovače.Vrací seznam seznamů. V každém podseznamu budou v řetězcích oddělení 'dd', 'mm', 'rrrr'
print(['/'.join(datum.split('.')) for datum in seznam])# rozdělí každý řetězec seznamu podle oddělovače '.' a vzniký seznam oddělených řetězců spiltem opět spojí znakem '/', výsledkem tedy bude řetězec 'dd/mm/rrrr'
