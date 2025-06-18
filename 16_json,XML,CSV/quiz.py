import http.client
import json
import html
import random

def get_questions(amount: int = 10, difficulty: str = 'easy') -> dict:
    """
    Busca perguntas de múltipla escolha da Open Trivia Database API.

    Args:
        amount (int): O número de perguntas a serem buscadas (padrão: 10).
        difficulty (str): A dificuldade das perguntas ('easy', 'medium', 'hard') (padrão: 'easy').

    Returns:
        dict: Um dicionário contendo os resultados da API, incluindo as perguntas.
    """
    conn = http.client.HTTPSConnection("opentdb.com")
    conn.request("GET", f"/api.php?amount={amount}&difficulty={difficulty}&type=multiple")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def parse_text(html_string: str) -> str:
    """
    Converte entidades HTML em caracteres normais.

    Args:
        html_string (str): A string contendo entidades HTML.

    Returns:
        str: A string com as entidades HTML decodificadas.
    """
    return html.unescape(html_string)


def start_quiz():
    """
    Inicia o jogo de quiz, buscando perguntas, apresentando-as ao usuário,
    coletando respostas e calculando a pontuação final.
    """
    print("--- Bem-vindo ao Quiz! ---")

    # Define a quantidade de perguntas e a dificuldade
    num_questions = 5
    quiz_difficulty = 'easy' # Você pode mudar para 'medium' ou 'hard'

    print(f"\nBuscando {num_questions} perguntas de dificuldade '{quiz_difficulty}'...")
    try:
        data = get_questions(amount=num_questions, difficulty=quiz_difficulty)
    except Exception as e:
        print(f"Ocorreu um erro ao buscar as perguntas: {e}")
        print("Verifique sua conexão com a internet ou tente novamente mais tarde.")
        return

    questions = data.get('results', [])

    if not questions:
        print("Não foi possível carregar as perguntas. Tente novamente.")
        return

    score = 0
    total_questions = len(questions)

    for i, q in enumerate(questions):
        question_text = parse_text(q['question'])
        correct_answer = parse_text(q['correct_answer'])
        incorrect_answers = [parse_text(ans) for ans in q['incorrect_answers']]

        all_answers = incorrect_answers + [correct_answer]
        random.shuffle(all_answers) # Mistura as opções de resposta

        print(f"\n--- Pergunta {i + 1}/{total_questions} ---")
        print(question_text)

        for j, answer_option in enumerate(all_answers):
            print(f"{j + 1}. {answer_option}")

        while True:
            try:
                user_choice = int(input("Sua resposta (digite o número): "))
                if 1 <= user_choice <= len(all_answers):
                    break
                else:
                    print("Opção inválida. Por favor, digite o número correspondente à sua escolha.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        selected_answer = all_answers[user_choice - 1]

        if selected_answer == correct_answer:
            print("Correto!")
            score += 1
        else:
            print(f"Errado! A resposta correta era: {correct_answer}")

    print("\n--- Quiz Finalizado! ---")
    print(f"Sua pontuação final: {score} de {total_questions}")
    print("Obrigado por jogar!")


start_quiz()
