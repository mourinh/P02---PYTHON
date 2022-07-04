def ver_prefixo(prefixo, palavra):
    tamanho = len(prefixo)
    if prefixo == palavra[:tamanho]:
        return True
    else:
        return False

print (ver_prefixo("Ca", "Cachorro"))
print (ver_prefixo("Pra", "Prada"))
print (ver_prefixo("Bat", "Boleiro"))