def status_aluno(notas):
    # Aqui estamos usando as notas passadas como argumento, ao invés de pedir input
    if len(notas) != 4:  # Verifica se a lista de notas tem exatamente 4 elementos
        return False

    try:
        média = sum(notas) / len(notas)
    except TypeError:
        return False

    print(média)
    if média >= 7:
        print("Foi aprovado")
        return True
    else:
        print("Foi reprovado")
        return False

def test():
    assert status_aluno([10, 10, 10, 10]) == True  # Aprovação
    assert status_aluno([10, 5, 10, 10]) == True   # Aprovação
    assert status_aluno([10, None, 10, 10]) == False  # Nota inválida (None)
    assert status_aluno([10, 5, None, 5]) == False  # Nota inválida (None)
    assert status_aluno([5, 5, 5, 5]) == False  # Reprovação (média abaixo de 7)
    assert status_aluno([0, 0, 0, 0]) == False  # Reprovação (média abaixo de 7)
