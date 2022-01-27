# jogo da forca

secreto = 'pipoca'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('=== Digite apenas uma letra ===')

    if letra in secreto:
        digitadas.append(letra)  # não pode palavra repetida (lembrar)
    else:
        chances -= 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)

    if chances == 0:
        print('Você perdeu! Tente outra vez.')
        break
    if secreto_temporario == secreto:
        print('Parabéns! Você acertou a palavra secreta: {}.'.format(secreto))
        break