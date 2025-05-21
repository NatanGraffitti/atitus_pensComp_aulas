NUMEROS = ("0123456789")

def obtem_dados_endereco(cep):
    import http.client
    import json

    url = f"/ws/{cep}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()
    # Exemplo de resposta
    # {
    #   'cep': '91110-000',
    #   'logradouro': 'Avenida Assis Brasil',
    #   'complemento': 'de 4000 a 6298 - lado par',
    #   'unidade': '',
    #   'bairro': 'São Sebastião',
    #   'localidade': 'Porto Alegre',
    #   'uf': 'RS',
    #   'ibge': '4314902',
    #   'gia': '',
    #   'ddd': '51',
    #   'siafi': '8801'
    # }
    return response


def validador_cep(cep):
    if len(cep) == 8:
        if all(char in NUMEROS for char in cep):
            return True
        else:
            return False

    if len(cep) == 9 and cep[5] == '-':
        parte1 = cep[:5]
        parte2 = cep[6:]
        if all(char in NUMEROS for char in parte1) and all(char in NUMEROS for char in parte2):
            return True
        else:
            return False

    return False

def add_endereco(cache, endereco):
    uf = endereco.get('uf')
    localidade = endereco.get('localidade')
    cep = endereco.get('cep')

    if uf is None or localidade is None:
        dados_completos = obtem_dados_endereco(cep)
        uf = dados_completos.get('uf', uf)
        localidade = dados_completos.get('localidade', localidade)
        cep = dados_completos.get('cep', cep)

    if uf is None or localidade is None or cep is None:
        return cache

    if uf not in cache:
        cache[uf] = {}

    if localidade not in cache[uf]:
        cache[uf][localidade] = []

    if cep not in cache[uf][localidade]:
        cache[uf][localidade].append(cep)

    return cache

def consulta_cep_com_cache(cache, cep):
    if cep in cache:
        return cache[cep]
    else:
        endereco = obtem_dados_endereco(cep)
        cache[cep] = endereco
        return endereco

def test():
    assert validador_cep("99110000")
    assert validador_cep("99110-000")
    assert not validador_cep("99110 000")
    assert not validador_cep("9911-0000")
    assert not validador_cep("99110000 ")
    assert not validador_cep(" 99110000")
    assert not validador_cep("9911000")

    endereco_01 = {
        "cep": "91110-000",
        "logradouro": "Avenida Assis Brasil",
        "localidade": "Porto Alegre",
        "uf": "RS",
    }
    endereco_02 = {
        "cep": "90240-111",
        "logradouro": "Rua Frederico Mentz",
        "localidade": "Porto Alegre",
    }
    resposta_01 = {"RS": {"Porto Alegre": ["91110-000"]}}
    assert add_endereco({}, endereco_01) == resposta_01
    assert add_endereco(resposta_01, endereco_01) == resposta_01
    assert add_endereco(resposta_01, endereco_02) == {
        "RS": {"Porto Alegre": ["91110-000", "90240-111"]}
    }
