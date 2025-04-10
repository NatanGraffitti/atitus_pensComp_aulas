def status_aluno(notas):
    a = int(input("qual a primeira nota do aluno?:"))
    b = int(input("digite a segunda:"))
    c = int(input("digite a terceira:"))
    d = int(input("digite a última:"))
    média = (a+b+c+d)/ 4
    print(média)
    if média >= 7:
     print("foi aprovado")
    else:
     print("foi reprovado")

def test():
 assert status_aluno([10, 10, 10, 10])
 assert status_aluno([10, None, 10, 10])

 assert not status_aluno([10, 5, None, 5])
 assert not status_aluno([5, 5, 5, 5])
 assert not status_aluno([0, 0, 0, 0])
