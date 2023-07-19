"""
Iterando strings com while
"""
#-------01234567891011
nome = 'Thiago Xavier' #Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1

print(novo_nome)

