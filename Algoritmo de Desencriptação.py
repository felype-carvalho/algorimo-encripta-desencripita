import string
letras = list(string.ascii_lowercase)

print('Bem-vindo ao programa de Desencriptação.')
palavra = input('Digite uma palavra para ser descriptografada: ')
tamanhoP = len(palavra)

crip = list(palavra)
palavra_crip = palavra

i = 0
h = 0
chave = 0

for chave in range(27):
    for i in range(tamanhoP):
        while palavra[i] != letras[h]:
            h = h + 1
        h = h - chave
        if h > 25:
            h = h - 26
        crip[i] = letras[h]
        h = 0
    palavra_crip = ''.join(crip)
    print("Chave: ", chave," = ", palavra_crip)

    
