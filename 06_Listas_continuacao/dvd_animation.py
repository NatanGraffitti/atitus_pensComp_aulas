def limpa_tela(): #DVD Animação
    import os  

    os.system("cls" if os.name == "nt" else "clear")  # Limpa o console
 

def espera():
    import time

    time.sleep(0.5)  # Espera meio segundo (500ms)


def desenha_tela(altura, largura, x, y, colisoes):
    limpa_tela()
    for i in range(altura):
        for j in range(largura):
            if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
                print("#", end="") 
            elif i == y and j == x:
                print("A", end="") 
            else:
                print(".", end="") 
        print()
    print(f"Colisões: {colisoes}")

altura = 10
largura = 20
x = 1
y = 1
colisoes = 0
direcao_x = 1
direcao_y = 1

while True:
    desenha_tela(altura, largura, x, y, colisoes)
    espera()

    x += direcao_x
    y += direcao_y

    if x == 0 or x == largura - 1:
        direcao_x *= -1
        colisoes += 1
    if y == 0 or y == altura - 1:
        direcao_y *= -1
        colisoes += 1
