def sao_anagramas(palavra1: str, palavra2: str) -> bool:
    if len(palavra1) != len(palavra2):
        return False

    return sorted(palavra1) == sorted(palavra2)

def test():
    assert sao_anagramas("amor", "roma")
    assert sao_anagramas("iracema", "america")
    assert sao_anagramas("estudo", "duetos")
    
    assert not sao_anagramas("banana", "anana")
    assert not sao_anagramas("banana", "")
    assert not sao_anagramas("banana", "abc")
