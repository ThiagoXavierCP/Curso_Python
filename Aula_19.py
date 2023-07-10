# Interpolação básica de strings 
# s - string
# de i - Int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789) 

nome = 'Thiago'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco) 
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
