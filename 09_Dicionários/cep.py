import http.client
import json
import re # Importar regex para validação de CEP mais robusta

# Constante para dígitos numéricos
NUMEROS = "0123456789" # É uma string, não uma tupla, para facilitar a verificação de 'in'

def obtem_dados_endereco(cep: str) -> dict | None:
    """
    Obtém os dados de endereço a partir de um CEP usando a API ViaCEP.

    Args:
        cep (str): O CEP a ser consultado (somente números ou com hífen).

    Returns:
        dict | None: Um dicionário com os dados do endereço se a consulta for bem-sucedida
                     e não houver erro no CEP, ou None em caso de erro ou CEP não encontrado.
    """
    # Remove qualquer caractere que não seja dígito para garantir o formato correto para a API
    cep_limpo = re.sub(r'\D', '', cep)

    conn = http.client.HTTPSConnection("viacep.com.br")
    try:
        url = f"/ws/{cep_limpo}/json/"
        conn.request("GET", url)
        response = conn.getresponse()
        response_text = response.read().decode()
        
        # Verifica o status da resposta HTTP
        if response.status != 200:
            print(f"Erro HTTP {response.status}: {response.reason} ao consultar CEP {cep}")
            return None

        data = json.loads(response_text)
        conn.close()

        # A API ViaCEP retorna {'erro': True} para CEPs não encontrados ou inválidos
        if data.get('erro'):
            print(f"CEP '{cep}' não encontrado ou inválido pela API.")
            return None
        
        return data
    except http.client.HTTPException as e:
        print(f"Erro de HTTP ao consultar CEP {cep}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON da resposta para CEP {cep}: {e}")
        print(f"Resposta recebida: {response_text[:200]}...") # Mostra um pedaço da resposta
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao obter dados do CEP {cep}: {e}")
        return None
    finally:
        # Garante que a conexão seja fechada mesmo se ocorrer um erro
        if conn:
            conn.close()


def validador_cep(cep: str) -> bool:
    """
    Valida o formato de um CEP, aceitando 8 dígitos ou 9 dígitos com hífen na quinta posição.

    Args:
        cep (str): O CEP a ser validado.

    Returns:
        bool: True se o CEP estiver no formato válido, False caso contrário.
    """
    # Usando regex para validação mais concisa e robusta
    # ^\d{8}$          -> 8 dígitos exatos
    # |                 -> OU
    # ^\d{5}-\d{3}$     -> 5 dígitos, um hífen, 3 dígitos exatos
    # re.fullmatch garante que a string inteira corresponda ao padrão
    return bool(re.fullmatch(r"^\d{8}$|^\d{5}-\d{3}$", cep))

def add_endereco(cache: dict, endereco: dict) -> dict:
    """
    Adiciona um endereço ao cache, organizando por UF e Localidade.
    Se UF ou Localidade estiverem faltando no dicionário `endereco`, tenta obtê-los
    usando a função `obtem_dados_endereco`.

    Args:
        cache (dict): O dicionário de cache atual.
        endereco (dict): Um dicionário contendo os dados do endereço (mínimo 'cep').

    Returns:
        dict: O dicionário de cache atualizado.
    """
    uf = endereco.get('uf')
    localidade = endereco.get('localidade')
    cep = endereco.get('cep')

    # Se o CEP não estiver presente ou não for válido, não podemos adicionar
    if not cep or not validador_cep(cep):
        print(f"CEP '{cep}' inválido ou ausente. Não foi possível adicionar ao cache.")
        return cache

    # Se UF ou localidade estiverem faltando, tenta buscar os dados completos
    if uf is None or localidade is None:
        print(f"UF ou Localidade ausentes para CEP {cep}. Tentando obter dados completos...")
        dados_completos = obtem_dados_endereco(cep)
        if dados_completos:
            uf = dados_completos.get('uf')
            localidade = dados_completos.get('localidade')
            # Atualiza o CEP no caso de ele vir normalizado da API (ex: 91110-000)
            cep = dados_completos.get('cep', cep)
        else:
            print(f"Não foi possível obter dados completos para o CEP {cep}. Não adicionado ao cache.")
            return cache

    # Se ainda assim UF ou Localidade forem None, não adiciona ao cache
    if uf is None or localidade is None:
        print(f"Dados essenciais (UF ou Localidade) ainda ausentes para CEP {cep}. Não adicionado ao cache.")
        return cache

    # Adiciona o endereço ao cache de forma hierárquica
    if uf not in cache:
        cache[uf] = {}

    if localidade not in cache[uf]:
        cache[uf][localidade] = []

    # Evita adicionar CEPs duplicados dentro da mesma lista de localidade
    if cep not in cache[uf][localidade]:
        cache[uf][localidade].append(cep)
        print(f"CEP {cep} de {localidade}/{uf} adicionado ao cache.")
    else:
        print(f"CEP {cep} já existe no cache para {localidade}/{uf}.")

    return cache


def consulta_cep_com_cache(cache: dict, cep: str) -> dict | None:
    """
    Consulta dados de um CEP, utilizando um cache para evitar requisições repetidas à API.

    Args:
        cache (dict): O dicionário de cache onde os dados dos CEPs já consultados são armazenados.
                      O formato do cache para esta função é {'cep': dados_endereco}.
        cep (str): O CEP a ser consultado.

    Returns:
        dict | None: Um dicionário com os dados do endereço, ou None se o CEP for inválido
                     ou a consulta à API falhar.
    """
    if not validador_cep(cep):
        print(f"CEP '{cep}' inválido. Por favor, forneça um CEP no formato 'DDDDDDDD' ou 'DDDDD-DDD'.")
        return None

    # Normaliza o CEP para ser usado como chave no cache (apenas dígitos)
    cep_normalizado = re.sub(r'\D', '', cep)
    
    if cep_normalizado in cache:
        print(f"CEP {cep_normalizado} encontrado no cache.")
        return cache[cep_normalizado]
    else:
        print(f"CEP {cep_normalizado} não encontrado no cache. Consultando API...")
        endereco_data = obtem_dados_endereco(cep_normalizado)
        if endereco_data:
            cache[cep_normalizado] = endereco_data
            print(f"Dados do CEP {cep_normalizado} adicionados ao cache.")
        return endereco_data

def test_functions():
    """
    Função para testar todas as funcionalidades desenvolvidas.
    """
    print("--- Iniciando Testes ---")

    # Testes para validador_cep
    print("\nTestando validador_cep:")
    assert validador_cep("99110000"), "Erro: 99110000 deveria ser válido"
    assert validador_cep("99110-000"), "Erro: 99110-000 deveria ser válido"
    assert not validador_cep("99110 000"), "Erro: 99110 000 não deveria ser válido"
    assert not validador_cep("9911-0000"), "Erro: 9911-0000 não deveria ser válido"
    assert not validador_cep("99110000 "), "Erro: '99110000 ' não deveria ser válido"
    assert not validador_cep(" 99110000"), "Erro: ' 99110000' não deveria ser válido"
    assert not validador_cep("9911000"), "Erro: 9911000 não deveria ser válido (curto)"
    assert not validador_cep("991100000"), "Erro: 991100000 não deveria ser válido (longo)"
    assert not validador_cep("abcde-fgh"), "Erro: abcde-fgh não deveria ser válido"
    assert not validador_cep("12345-abc"), "Erro: 12345-abc não deveria ser válido"
    print("Todos os testes de validador_cep passaram!")

    # Testes para add_endereco
    print("\nTestando add_endereco:")
    cache_enderecos = {}
    
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
        # UF será buscada pela função
    }
    endereco_03 = { # Novo CEP para adicionar outra localidade/UF
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "localidade": "São Paulo",
        "uf": "SP",
    }
    endereco_invalido = {
        "cep": "123", # CEP inválido
        "localidade": "Cidade Teste",
        "uf": "XX"
    }

    # Teste 1: Adicionar o primeiro endereço
    cache_result_1 = add_endereco({}, endereco_01.copy())
    expected_cache_1 = {"RS": {"Porto Alegre": ["91110-000"]}}
    assert cache_result_1 == expected_cache_1, f"Erro no Teste 1: {cache_result_1} != {expected_cache_1}"
    print(f"Cache após adicionar 91110-000: {cache_result_1}")

    # Teste 2: Adicionar o mesmo endereço novamente (não deve mudar)
    cache_result_2 = add_endereco(cache_result_1.copy(), endereco_01.copy())
    assert cache_result_2 == expected_cache_1, f"Erro no Teste 2: {cache_result_2} != {expected_cache_1}"
    print(f"Cache após adicionar 91110-000 novamente: {cache_result_2}")

    # Teste 3: Adicionar um segundo endereço para a mesma localidade/UF (com UF/Localidade faltando)
    cache_result_3 = add_endereco(cache_result_2.copy(), endereco_02.copy())
    expected_cache_3 = {"RS": {"Porto Alegre": ["91110-000", "90240-111"]}}
    # Ordena as listas para garantir que a comparação seja justa
    for uf_key in cache_result_3:
        for loc_key in cache_result_3[uf_key]:
            cache_result_3[uf_key][loc_key].sort()
    for uf_key in expected_cache_3:
        for loc_key in expected_cache_3[uf_key]:
            expected_cache_3[uf_key][loc_key].sort()

    assert cache_result_3 == expected_cache_3, f"Erro no Teste 3: {cache_result_3} != {expected_cache_3}"
    print(f"Cache após adicionar 90240-111: {cache_result_3}")

    # Teste 4: Adicionar um endereço para uma nova UF/Localidade
    cache_result_4 = add_endereco(cache_result_3.copy(), endereco_03.copy())
    expected_cache_4 = {
        "RS": {"Porto Alegre": ["91110-000", "90240-111"]},
        "SP": {"São Paulo": ["01001-000"]}
    }
    # Ordena as listas para garantir que a comparação seja justa
    for uf_key in cache_result_4:
        for loc_key in cache_result_4[uf_key]:
            cache_result_4[uf_key][loc_key].sort()
    for uf_key in expected_cache_4:
        for loc_key in expected_cache_4[uf_key]:
            expected_cache_4[uf_key][loc_key].sort()

    assert cache_result_4 == expected_cache_4, f"Erro no Teste 4: {cache_result_4} != {expected_cache_4}"
    print(f"Cache após adicionar 01001-000: {cache_result_4}")

    # Teste 5: Adicionar um CEP inválido (não deve alterar o cache)
    initial_cache_for_invalid = cache_result_4.copy()
    cache_result_5 = add_endereco(initial_cache_for_invalid, endereco_invalido)
    assert cache_result_5 == initial_cache_for_invalid, "Erro: CEP inválido não deveria alterar o cache"
    print("Teste de CEP inválido para add_endereco passou (cache inalterado).")

    print("Todos os testes de add_endereco passaram!")

    # Testes para consulta_cep_com_cache
    print("\nTestando consulta_cep_com_cache:")
    api_cache = {} # Cache separado para consulta_cep_com_cache

    # Teste 1: Primeira consulta de um CEP (deve ir à API)
    cep_consulta_1 = "91110-000"
    result_1 = consulta_cep_com_cache(api_cache, cep_consulta_1)
    assert result_1 is not None and result_1.get('cep') == "91110-000", f"Erro na consulta 1: {result_1}"
    assert re.sub(r'\D', '', cep_consulta_1) in api_cache, "CEP não adicionado ao cache após primeira consulta."
    print(f"Consulta 1 para {cep_consulta_1} bem-sucedida. Cache: {api_cache.keys()}")

    # Teste 2: Segunda consulta do mesmo CEP (deve vir do cache)
    cep_consulta_2 = "91110000" # Formato diferente, mas mesmo CEP
    result_2 = consulta_cep_com_cache(api_cache, cep_consulta_2)
    assert result_2 is not None and result_2.get('cep') == "91110-000", f"Erro na consulta 2: {result_2}"
    print(f"Consulta 2 para {cep_consulta_2} bem-sucedida (do cache). Cache: {api_cache.keys()}")

    # Teste 3: Consulta de um novo CEP (deve ir à API)
    cep_consulta_3 = "01001-000"
    result_3 = consulta_cep_com_cache(api_cache, cep_consulta_3)
    assert result_3 is not None and result_3.get('cep') == "01001-000", f"Erro na consulta 3: {result_3}"
    assert re.sub(r'\D', '', cep_consulta_3) in api_cache, "Novo CEP não adicionado ao cache."
    print(f"Consulta 3 para {cep_consulta_3} bem-sucedida. Cache: {api_cache.keys()}")

    # Teste 4: Consulta de um CEP inválido (não deve retornar dados nem adicionar ao cache)
    cep_consulta_invalido = "12345"
    result_invalido = consulta_cep_com_cache(api_cache, cep_consulta_invalido)
    assert result_invalido is None, f"Erro: CEP inválido deveria retornar None, mas retornou {result_invalido}"
    assert re.sub(r'\D', '', cep_consulta_invalido) not in api_cache, "CEP inválido adicionado ao cache."
    print("Consulta de CEP inválido testada com sucesso.")

    # Teste 5: Consulta de um CEP que a API retorna 'erro': true (não deve retornar dados)
    cep_nao_existente = "99999999" # Geralmente inexistente
    result_nao_existente = consulta_cep_com_cache(api_cache, cep_nao_existente)
    assert result_nao_existente is None, f"Erro: CEP inexistente deveria retornar None, mas retornou {result_nao_existente}"
    print("Consulta de CEP inexistente (API retorna erro) testada com sucesso.")


    print("\n--- Todos os testes concluídos! ---")

# Executa os testes
if __name__ == "__main__":
    test_functions()
