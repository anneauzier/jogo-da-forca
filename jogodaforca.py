# jogo da forca

secreto = 'chocolate'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in secreto:
        digitadas.append(letra)
    else:
        chances -= 1
        print('Você tem {} chances'.format(chances))

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario = secreto_temporario + letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)

    if secreto_temporario == secreto:
        print('Parabéns, você acertou a palavra secreta: {}!!'.format(secreto))
        break

    if chances == 0:
        print('Você perdeu suas chances :(')
        break