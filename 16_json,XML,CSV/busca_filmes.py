import http.client
import json

def get_movies(texto_busca: str) -> dict:
    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)

def search_movie(movie_name: str) -> dict:
    """
    Busca um filme pelo nome usando a função get_movies e retorna o resultado completo da API.
    Se nenhum filme for encontrado ou a API retornar um formato inesperado, pode retornar um dicionário vazio ou uma mensagem de erro.
    """
    if not movie_name:
        return {"error": "Nome do filme não pode ser vazio."}

    try:
        data = get_movies(movie_name)
        # A estrutura do retorno da API pode variar, mas geralmente 'results' ou 'Search' são chaves comuns.
        # Vamos assumir que a API retorna um dicionário com uma chave 'results' contendo uma lista de filmes.
        if data and 'results' in data and len(data['results']) > 0:
            # Retorna o primeiro filme encontrado, ou a lista completa se preferir
            return data['results'][0] # Retorna o primeiro filme da lista de resultados
        elif data and 'Search' in data and len(data['Search']) > 0:
            return data['Search'][0] # Caso a chave seja 'Search'
        else:
            return {"message": "Nenhum filme encontrado com esse nome."}
    except Exception as e:
        return {"error": f"Ocorreu um erro ao buscar o filme: {e}"}

# Exemplo de uso:
# filme_encontrado = search_movie("Interestellar")
# print(filme_encontrado)
