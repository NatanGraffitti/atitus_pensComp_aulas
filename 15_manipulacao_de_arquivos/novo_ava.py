import os
import re

def limpa_nome_pasta(nome: str) -> str:
    nome = nome.lower()
    nome = nome.replace(" ", "_")
    nome = re.sub(r'[^a-z0-9_]', '', nome)
    return nome

def test_limpa_nome_pasta(): 
    assert limpa_nome_pasta('Ciência da Computação') == 'ciencia_da_computacao'
    assert limpa_nome_pasta('Administração') == 'administracao'

def cria_pasta_curso(nome_curso: str) -> None:
    pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print(f"A pasta '{pasta}' foi criada com sucesso.")
    else:
        print(f"A pasta '{pasta}' já existe.")

def test_cria_pasta_curso():
    nome = "Teste Curso"
    pasta = limpa_nome_pasta(nome)
    if os.path.exists(pasta):
        os.rmdir(pasta)
    cria_pasta_curso(nome)
    assert os.path.exists(pasta)
    os.rmdir(pasta)

def cria_alunos(alunos: list, nome_curso: str) -> None:
    pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    caminho_arquivo = os.path.join(pasta, "alunos.txt")
    with open(caminho_arquivo, "w", encoding="utf-8") as f: 
        for aluno in alunos:
            f.write(aluno + "\n")
    print(f"Arquivo 'alunos.txt' criado com {len(alunos)} alunos na pasta '{pasta}'.")

def test_cria_alunos():
    nome_curso = "Curso Teste"
    alunos = ["Ana", "João", "Maria"]
    pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    cria_alunos(alunos, nome_curso)
    caminho = os.path.join(pasta, "alunos.txt")
    assert os.path.exists(caminho)
    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
    assert linhas == alunos
    os.remove(caminho)
    os.rmdir(pasta)

def converte_alunos_em_lista(alunos_com_virgula: str) -> list:
    lista = [aluno.strip() for aluno in alunos_com_virgula.split(",") if aluno.strip()]
    return lista

def test_converte_alunos_em_lista():
    assert converte_alunos_em_lista("Ana, João, Maria") == ["Ana", "João", "Maria"]
    assert converte_alunos_em_lista("  Ana ,João , Maria ") == ["Ana", "João", "Maria"]
    assert converte_alunos_em_lista("Ana,, João,,") == ["Ana", "João"]
    assert converte_alunos_em_lista("") == []
