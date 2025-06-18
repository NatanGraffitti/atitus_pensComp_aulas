import re

# Constante para a idade de maioridade
IDADE_PARA_MAIORIDADE = 18

def verifica_maioridade(idade: int) -> bool:
    """
    Verifica se a idade fornecida é igual ou superior à idade de maioridade.

    Args:
        idade (int): A idade a ser verificada.

    Returns:
        bool: True se a idade for maior ou igual à idade de maioridade, False caso contrário.
    """
    return idade >= IDADE_PARA_MAIORIDADE

def verifica_email(email: str) -> bool:
    """
    Verifica se o formato do e-mail é válido, seguindo um padrão básico.
    Permite letras (maiúsculas/minúsculas), números e underscore antes do @ e no domínio.
    Suporta múltiplos subdomínios (ex: .com.br).

    Args:
        email (str): A string do e-mail a ser verificada.

    Returns:
        bool: True se o e-mail for considerado válido, False caso contrário.
    """
    # Expressão regular para validar o formato do e-mail.
    # [a-zA-Z0-9_]+  -> Pelo menos um caractere alfanumérico ou underscore (usuário)
    # @             -> O símbolo arroba
    # [a-zA-Z0-9_]+ -> Pelo menos um caractere alfanumérico ou underscore (domínio)
    # \.            -> Um ponto literal
    # [a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})* -> TLD de 2 ou mais letras, opcionalmente seguido
    #                                  por mais subdomínios (ex: .com.br)
    pattern = re.compile(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$")

    # Verifica se o email atende a critérios básicos de formato que a regex pode não pegar:
    if '@' not in email or '.' not in email:
        return False
    if email.startswith('@') or email.endswith('.') or email.endswith('@'):
        return False
    if '@@' in email or '.@' in email or '@.' in email:
        return False
    
    # Valida usando a expressão regular
    return bool(pattern.match(email))

def solicita_nome() -> str | None:
    """
    Solicita ao usuário que digite seu nome.

    Returns:
        str | None: O nome digitado pelo usuário, ou None se o campo for deixado em branco.
    """
    name = input("Por favor, digite seu nome: ").strip()
    if name:
        return name
    return None

def main():
    """
    Função principal que orquestra o processo de cadastro,
    utilizando as funções de validação.
    """
    print("--- Bem-vindo(a) ao Sistema de Cadastro Simplificado! ---")

    # 1. Solicita e valida o nome
    nome_usuario = None
    while nome_usuario is None:
        nome_usuario = solicita_nome()
        if nome_usuario is None:
            print("O nome não pode estar em branco. Por favor, tente novamente.")

    print(f"\nOlá, {nome_usuario}!")

    # 2. Solicita e valida a idade
    idade_valida = False
    idade_usuario = 0
    while not idade_valida:
        try:
            idade_input = input("Por favor, digite sua idade: ")
            idade_usuario = int(idade_input)
            if idade_usuario < 0:
                print("A idade não pode ser um número negativo. Por favor, tente novamente.")
            elif not verifica_maioridade(idade_usuario):
                print(f"Você precisa ter {IDADE_PARA_MAIORIDADE} anos ou mais para se cadastrar.")
            else:
                idade_valida = True
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a idade.")

    print(f"Idade ({idade_usuario} anos) verificada com sucesso!")

    # 3. Solicita e valida o e-mail
    email_valido = False
    email_usuario = ""
    while not email_valido:
        email_usuario = input("Por favor, digite seu e-mail: ").strip()
        if not verifica_email(email_usuario):
            print("Formato de e-mail inválido. Por favor, tente novamente (ex: usuario@dominio.com).")
        else:
            email_valido = True

    print(f"E-mail ({email_usuario}) verificado com sucesso!")

    print("\n--- Cadastro Concluído com Sucesso! ---")
    print(f"Nome: {nome_usuario}")
    print(f"Idade: {idade_usuario} anos")
    print(f"E-mail: {email_usuario}")
    print("Obrigado por se cadastrar!")

# Executa a função principal
if __name__ == "__main__":
    main()

def test_verifica_maioridade():    
    assert not verifica_maioridade(-1)
    assert not verifica_maioridade(0)
    assert not verifica_maioridade(1)
    assert not verifica_maioridade(17)
    assert verifica_maioridade(18)
    assert verifica_maioridade(20)
    assert verifica_maioridade(100)

def test_verifica_email():    
    assert not verifica_email('')
    assert not verifica_email('@')
    assert not verifica_email('@@')
    assert not verifica_email('abc@@abc.com')
    assert not verifica_email('abc@abc.edu')
    assert not verifica_email('a_b_c@a_b_c.com.com')
    assert not verifica_email('a_b_c@a_b_c.com.com.com')

    assert verifica_email('ABC@a_b_c.com')
    assert verifica_email('ABC@ABC.com')
    assert verifica_email('AbC@1BC.com')
    assert verifica_email('abc@abc.com')
    assert verifica_email('a23@123.com')
    assert verifica_email('a_b_c@a_b_c.com')
