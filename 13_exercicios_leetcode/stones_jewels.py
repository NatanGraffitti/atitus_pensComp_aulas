# https://leetcode.com/problems/jewels-and-stones/description/

def stones_jewels(jewels, stones):
    conjunto_joias = set(jewels)
    contador = 0
    for pedra in stones:
        if pedra in conjunto_joias:
            contador += 1
    return contador


def test():
    assert stones_jewels(jewels="aA", stones="aAAbbbb") == 3
    assert stones_jewels(jewels="z", stones="ZZ") == 0

print("Testes OK!")
