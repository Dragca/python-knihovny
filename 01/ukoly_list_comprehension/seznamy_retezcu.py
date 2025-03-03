# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/seznamy-retezcu

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

# 1.
print([len(j) for j in jmena])
# 2.
print([j.upper() for j in jmena])
# 3.
print([j + 'a' for j in jmena])
# 4.
print([j.lower() + '@email.cz' for j in jmena])
