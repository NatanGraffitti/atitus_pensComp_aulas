from typing import Optional 

def saudacao(nome: str, sobrenome: Optional[str] = None, titulo: str = 'Sr.'): -> str:
    if nome == '':    
        return "Olá!"    
    if sobrenome is None:
        return f"Olá, {titulo} {nome}"
    else: 
        return f"Olá, {titulo} {nome} {sobrenome}"

def test():
    assert saudacao("Matheus") == "Olá, Sr. Matheus"
    assert saudacao("Matheus", "Jardim") == "Olá, Sr. Matheus Jardim"
    assert saudacao("Matheus", "Jardim", "Prof") == "Olá, Prof Matheus Jardim"
    assert saudacao("Matheus", titulo="Prof") == "Olá, Prof Matheus"
    assert saudacao("") == "Olá!"
