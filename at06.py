def contador_strings(strings, letra):
    contador = 0
    for item in strings:
        if item == letra:
            contador += 1
    return contador
print(contador_strings("responde ai mano blz ai mano vem ai", "a"))
