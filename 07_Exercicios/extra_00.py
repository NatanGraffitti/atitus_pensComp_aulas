def saudacao(nome, sobrenome, ano_nascimento):
    ANO_ATUAL = 2025
    nome = input('Qual o seu nome?')
    sobrenome = input('Qual o seu sobrenome?')
    data_de_nascimento = int(input('Qual o seu ano de nascimento?'))
    idade = ANO_ATUAL - data_de_nascimento 

print('Olá,', '" nome, sobrenome "', 'você tem: ', idade, 'anos')

def test():
assert (
    saudacao("Matheus", "Jardim", 1991)
    == "Olá, Matheus Jardim. Bom dia! Você possui 33 anos!"
)
assert (
    saudacao("Thais", "Silva", 1990)
    == "Olá, Thais Silva. Bom dia! Você possui 34 anos!"
)
assert saudacao("Matheus", "Jardim", 0) is None
assert saudacao("Matheus", "Jardim", 2050) is None
