import string
letras = list(string.ascii_lowercase)

print('Bem-vindo ao programa de criptação.')
palavra = input('Digite uma palavra para ser criptografada: ')
chave = eval(input('Digite uma chave: '))

crip = list(palavra)
palavra_crip = palavra
i = 0
h = 0

for i in range(len(palavra)):
    
    while palavra[i] != letras[h]:
        h = h + 1
        
    h = h + chave
    
    while h >= 26:
        h = h - 26
        
    while h < 0:
        h = h + 26

    crip[i] = letras[h]
    h = 0
    
palavra_crip=''.join(crip)
print('Palavra criptografada: ', palavra_crip)
