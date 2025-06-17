INTRODUCOES = [
    "Tudo bem? É o seguinte...",
    "Você não vai acreditar, mas",
    "Nem imagina o que vou te contar:",
    "Parece mentira mas",
    "Tentar eu tentei, porém",
    "Eu até queria, mas",
]

OBJETOS = [
    "a Steam",
    "o dungeon master",
    "o Mark Zuckerberg",
    "o cachorro do vizinho",
    "meu pokemon favorito",
    "o ET Bilú",
    "o Zé Gotinha",
]
EVENTOS = [
    "roubou minha bicicleta",
    "hackeou meu instagram",
    "nerfou meu mago lv 30",
    "me venceu com o Exódia",
    "não sabe tocar piano",
    "pôs meu nome no Death Note",
]


def string_aleatoria(opcoes: list) -> str:
    return random.choice(opcoes)


def gerador_desculpas(tarefa: str) -> str:
    introducao = string_aleatoria(INTRODUCOES)
    objeto = string_aleatoria(OBJETOS)
    evento = string_aleatoria(EVENTOS)
    return f"{introducao} {objeto} {evento}, então não consegui {tarefa}."


# Exemplo de uso
print(gerador_desculpas("fazer o trabalho de casa"))
