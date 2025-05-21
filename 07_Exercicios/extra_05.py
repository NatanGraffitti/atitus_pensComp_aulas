def status_aluno(notas): 
    if None in notas:
        return False 
    
    todas_10 = True
    for nota in notas:
        if nota != 10:
            todas_10 = False
            break
    
    if todas_10:
        return True
    
    total = 0
    quantidade = 0
    for nota in notas:
        total += nota
        quantidade += 1
    
    if quantidade == 0:
        return False
    
    media = total / quantidade
    
    if media >= 7:  
        return True
    return False

notas_input = input("Digite as notas separadas por vírgula: ")
notas = [float(nota) if nota.lower() != "none" else None for nota in notas_input.split(",")]  # Converte notas para lista de floats, tratando 'None'

status = status_aluno(notas)

if status:
    print("O aluno passou!")
else:
    print("O aluno não passou.")


def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])

    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])
