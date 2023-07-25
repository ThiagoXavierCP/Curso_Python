frase = 'O Python é uma linguagem de programação \
    multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

i = 0 
apareceu_mais_vzs = 0
letra_apareceu_mais_vzs = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qnts_vzs_letra_apareceu = frase.count(letra_atual)

    if apareceu_mais_vzs < qnts_vzs_letra_apareceu:
        apareceu_mais_vzs = qnts_vzs_letra_apareceu
        letra_apareceu_mais_vzs = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vzs}" que apareceu '
      f'{apareceu_mais_vzs}x'
      )