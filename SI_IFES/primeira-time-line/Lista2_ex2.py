# LISTA 2 - Ex. 2

# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra, escrever: F - Feminino, M - Masculino ou Sexo Inválido.

sexo = input('Informe "M" p/ MASCULINO ou "F" p/ FEMININO: ')

if sexo == 'F' or sexo == 'f':
    print('F - Feminino')
elif sexo == 'M' or sexo == 'm':
    print('M - Masculino')
else:
    print('Sexo inválido')
    
