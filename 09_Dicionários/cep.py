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
    if len(cep) == 9:
        cep = cep.replace('-', '')
    if len(cep) != 8:
        return False
    try:
        int(cep)
        return true
    except:
        return False


def add_endereco(cache, endereco):
    pass

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
def test():
    assert add_endereco({}, endereco_01) == resposta_01
    assert add_endereco(resposta_01, endereco_01) == resposta_01
    assert add_endereco(resposta_01, endereco_02) == {
    "RS": {"Porto Alegre": ["91110-000", "90240-111"]}
}
