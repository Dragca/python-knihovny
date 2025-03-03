# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/seznam-teplot
from statistics import mean

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# 1. pruměrné t pro každý den
print([sum(t) / len(t) for t in teploty])
# 1. pomocí mean
print([mean(t) for t in teploty])
# 2. ranní t
print([t[0] for t in teploty])
# 3. noční t
print([t[-1] for t in teploty])
# 4. seznam dvouprvkových seznamů obsahující pouze polední a noční t
print([[t[1], t[-1],] for t in teploty])
