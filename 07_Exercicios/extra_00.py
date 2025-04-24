def saudacao(nome, sobrenome, ano_nascimento):
    ANO_ATUAL = 2025

    # O ano de nascimento precisa ser maior que zero e não pode ser no futuro
    if ano_nascimento <= 0 or ano_nascimento > ANO_ATUAL:
        return None
        
    idade = ANO_ATUAL - ano_nascimento
    
    return f"Olá, {nome} {sobrenome}. Bom dia! Você possui {idade} anos!"

def test():
    assert saudacao("Matheus", "Jardim", 1991)  #"Olá, Matheus Jardim. Bom dia! Você possui 34 anos!"
    assert saudacao("Matheus", "Jardim", 1990)  #"Olá, Matheus Jardim. Bom dia! Você possui 35 anos!"
    assert saudacao("Matheus", "Jardim", 0) is None
    assert saudacao("Matheus", "Jardim", 2050) is None
    print("Todos os testes passaram!")

print(saudacao("Matheus", "Jardim", 2000)) 
