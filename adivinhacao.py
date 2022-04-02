import random
while True:

    print('****************************************')
    print('Olá Mun-do! Meu primeiro jogo com Python!')
    print('   Bem vindo ao jogo da Adivinhação!')
    print('****************************************')

    numero_secreto = random.randint(1, 100)
    adivinhacao = int(input('Digite o seu número (de 1 a 100): '))

    print('Você digitou', adivinhacao)

    usuario_acertou = adivinhacao == numero_secreto
    numero_maior = adivinhacao > numero_secreto
    numero_menor = adivinhacao < numero_secreto

    if usuario_acertou:
        print('Parabéns! Você acertou!! :D')
    else:
        if numero_maior:
            print('Você errou! O seu chute foi maior do que o número secreto.')
        if numero_menor:
            print('Você errou! O seu chute foi menor do que o número secreto.')

    m = input('Você deseja continuar?[Sim/Não]').strip().lower()
    while m not in 'simnão':
        m = str(input('Erro: comando não reconhecido'))
    if m == 'sim':
        continue
    else:
        break
