# Napište program, který dostane na příkazovém řádku název proměnné v hadí notaci a vrátí tentýž název zapsaný ve velbloudí notaci.
# Příklad:
# python had-velbloud.py had_honi_velblouda
# hadHoniVelblouda

import sys

if len(sys.argv) != 2:
    exit(f"Usage:{sys.argv[0]} <rezetezec>")

# modified using string functions
snake = sys.argv[1]
words = snake.split('_')  # splits a string into individual words based on a delimiter and returns a list of words
# print([slovo.capitalize() for slovo in words[1:]]) - tried list comprehension
print(words[0] + "".join(w.capitalize() for w in words[1:]))
