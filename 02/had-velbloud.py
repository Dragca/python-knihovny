# Napište program, který dostane na příkazovém řádku název proměnné v hadí notaci a vrátí tentýž název zapsaný ve velbloudí notaci.
# Příklad:
# python had-velbloud.py had_honi_velblouda
# hadHoniVelblouda

import sys

if len(sys.argv) != 2:
    exit(f"Usage:{sys.argv[0]} <rezetezec>")


def change_string(string):
    prev_char = ''
    new_string = ''

    for char in string:
        if prev_char == '_':
            char = char.upper()
        prev_char = char
        if char != '_':
            new_string += char

    return new_string

print(change_string(sys.argv[1]))
