import http.client  # Módulo para fazer requisições HTTP/HTTPS
import json         # Módulo para trabalhar com dados JSON

def get_response(coin_a: str, coin_b: str) -> dict:
    """
    Faz uma requisição à API da Coinbase para obter o preço de compra
    da coin_a em termos da coin_b.

    Args:
        coin_a (str): O símbolo da criptomoeda base (ex: "BTC", "ETH").
        coin_b (str): O símbolo da moeda de destino (ex: "USD", "BRL").

    Returns:
        dict: Um dicionário contendo a resposta JSON da API.
              Em caso de erro, pode conter uma chave 'errors'.
              Em sucesso, contém uma chave 'data' com 'base', 'currency' e 'amount'.
    """
    try:
        conn = http.client.HTTPSConnection("api.coinbase.com")
        # Caminho da API para obter o preço de compra de uma moeda em relação a outra
        conn.request("GET", f"/v2/prices/{coin_a}-{coin_b}/buy")
        response = conn.getresponse()
        response_text = response.read().decode('utf-8') # Decodifica a resposta para string
        conn.close()
        return json.loads(response_text)
    except Exception as e:
        # Em caso de qualquer erro de conexão ou JSON, retorna um erro customizado
        return {"errors": [{"id": "connection_error", "message": f"Erro de conexão ou parse: {e}"}]}


def get_exchange_rate(coin_a: str, coin_b: str) -> float:
    """
    Extrai a taxa de câmbio de compra (o "amount") da resposta da API da Coinbase.

    Args:
        coin_a (str): A criptomoeda base (ex: "BTC").
        coin_b (str): A moeda alvo (ex: "USD").

    Returns:
        float: A taxa de câmbio como um número de ponto flutuante.
               Retorna 0.0 se ocorrer um erro ou a taxa não puder ser obtida.
    """
    # Chama a função para obter a resposta da API
    response = get_response(coin_a, coin_b)
    
    # Verifica se há erros na resposta da API
    if "errors" in response:
        # print(f"Erro ao obter a taxa de câmbio para {coin_a}-{coin_b}: {response['errors'][0]['message']}")
        return 0.0 # Retorna 0.0 para indicar falha

    # Tenta extrair o valor da taxa de câmbio
    if "data" in response and "amount" in response["data"]:
        try:
            return float(response["data"]["amount"])
        except ValueError:
            # print(f"Não foi possível converter o valor '{response['data']['amount']}' para float.")
            return 0.0
    
    # Se a estrutura de dados esperada não for encontrada
    # print(f"Estrutura de dados inesperada na resposta da API para {coin_a}-{coin_b}.")
    return 0.0


def get_new_value(coin_a: str, coin_b: str, value: float) -> float:
    """
    Calcula o valor equivalente de uma quantia de `coin_a` em `coin_b`,
    usando a taxa de câmbio de compra atual.

    Args:
        coin_a (str): A criptomoeda de origem (ex: "BTC").
        coin_b (str): A moeda de destino (ex: "USD").
        value (float): A quantia de `coin_a` a ser convertida.

    Returns:
        float: O valor convertido em `coin_b`.
               Retorna 0.0 se a taxa de câmbio não puder ser obtida
               ou o valor de entrada for inválido.
    """
    # Valida se o valor de entrada é um número não negativo
    if not isinstance(value, (int, float)) or value < 0:
        # print("Valor de entrada inválido. Deve ser um número não negativo.")
        return 0.0

    # Obtém a taxa de câmbio usando a função auxiliar
    exchange_rate = get_exchange_rate(coin_a, coin_b)

    # Verifica se a taxa de câmbio é válida (maior que zero)
    if exchange_rate > 0:
        return value * exchange_rate
    else:
        # print(f"Não foi possível obter uma taxa de câmbio válida para {coin_a}-{coin_b}.")
        return 0.0

---

## Exemplos de Uso

Aqui estão alguns exemplos de como você pode usar as funções acima para obter e converter valores de criptomoedas.

```python
if __name__ == "__main__":
    print("--- Verificando taxas de câmbio e convertendo valores ---")

    # Exemplo 1: Bitcoin (BTC) para Dólar Americano (USD)
    print("\n--- BTC para USD ---")
    btc_usd_rate = get_exchange_rate("BTC", "USD")
    if btc_usd_rate > 0:
        print(f"Taxa de compra: 1 BTC = {btc_usd_rate:.2f} USD")
        
        # Valor a ser convertido
        btc_quantidade = 0.05
        usd_equivalente = get_new_value("BTC", "USD", btc_quantidade)
        if usd_equivalente > 0:
            print(f"{btc_quantidade} BTC equivalem a {usd_equivalente:.2f} USD")
        else:
            print(f"Não foi possível converter {btc_quantidade} BTC para USD.")
    else:
        print("Não foi possível obter a taxa de câmbio BTC-USD.")

    # Exemplo 2: Ethereum (ETH) para Real Brasileiro (BRL)
    print("\n--- ETH para BRL ---")
    eth_brl_rate = get_exchange_rate("ETH", "BRL")
    if eth_brl_rate > 0:
        print(f"Taxa de compra: 1 ETH = {eth_brl_rate:.2f} BRL")

        # Valor a ser convertido
        eth_quantidade = 0.1
        brl_equivalente = get_new_value("ETH", "BRL", eth_quantidade)
        if brl_equivalente > 0:
            print(f"{eth_quantidade} ETH equivalem a {brl_equivalente:.2f} BRL")
        else:
            print(f"Não foi possível converter {eth_quantidade} ETH para BRL.")
    else:
        print("Não foi possível obter a taxa de câmbio ETH-BRL. Verifique se o par é suportado ou a API está fora do ar.")

    # Exemplo 3: Par de moedas inexistente (XRP-XYZ)
    print("\n--- XRP para XYZ (par inexistente) ---")
    xrp_xyz_rate = get_exchange_rate("XRP", "XYZ")
    if xrp_xyz_rate == 0.0:
        print("Taxa de câmbio XRP-XYZ retornou 0.0, como esperado para um par inexistente ou erro.")
    
    # Exemplo 4: Entrada inválida
    print("\n--- Entrada inválida ---")
    valor_invalido = get_new_value("BTC", "USD", -10.0)
    if valor_invalido == 0.0:
        print("Valor de entrada negativo resultou em 0.0, como esperado.")
