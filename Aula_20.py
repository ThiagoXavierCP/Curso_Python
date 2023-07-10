# Interpolação básica de strings 
# s - string
# d - Int
# f - float
# .<numero de digitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(qunatidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # Move o valor 10 casas depois
print(f'{variavel: <10}') # Move o valor 10 antes depois
print(f'{variavel:0^10}.') # Preenche as casas com 0
print(f'{1000.45474572345:.2f}')