import random
cont = 3
numero_secreto = random.randint(1, 100)

print('****************************************')
print('Olá Mun-do! Meu primeiro jogo com Python!')
print('   Bem vindo ao jogo da Adivinhação!')
print('****************************************')
print("You have 3 chances! Let's go ->")

while True:
    adivinhacao = int(input('Digite o seu número (de 1 a 100): '))
  
    print()
    print("*"*40)
    print('Você digitou', adivinhacao)
    print("*"*40)

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
    cont -= 1
    if cont == 0:
      print("This was ur last chance, gg, bye!")
      break
    else:
      m = input(f'You have {cont} last chance(s). Você deseja continuar?[S/N]').strip().lower()
      while m not in 'ysn':
        print("Error 404: Command Not Found!")
        m = input('Try writing again, do you want to continue?[Y/N] ').strip().lower()
      if m in 'sy':
        pass
      else:
        break

print('Fim do jogo!')
