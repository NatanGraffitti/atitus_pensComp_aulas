def desenha_losango(altura):
    # altura par = incrementa +1 para garantir o losango corretamente feito 
    # convertendo de string para inteiro MUITO IMPORTANTE
    if altura % 2 == 0:  # divisao da altura por 2 com resto zero == par
        altura += 1  # altura recebe +1
        print('O valor digitado era par, usaremos', altura, 'no lugar')

    meio = altura // 2  # considerando que a contagem inicia em 0, essa variável declara o meio do losango

    for linha_atual in range(altura):  
        # itera de zero ate a altura definida 
        # RANGE FORMA UMA LISTA, SEMPRE UMA LISTA começando do ZERO == (se for 3 = 0, 1, 2)

        if linha_atual <= meio:  # se a linha for menor ou igual ao meio
            num_espacos = meio - linha_atual  # numero de espaços recebe o valor de meio menos a linha do loop
            num_star = linha_atual * 2 + 1  # cria uma variavel que recebe o que vai ser produzido
                                            # recebe o valor de linha_atual e multiplica por 2, adiciona 1 --> aumento da contagem
        else:  
            # marca o meio do losango, ele só começa a ser usado a partir do momento que linha_atual passa a ser maior que meio
            num_espacos = linha_atual - meio
            num_star = altura - (linha_atual - meio) * 2

        print(' ' * num_espacos + '#' * num_star)
