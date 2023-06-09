# Utilize a função acima para gerar 50 números aleatórios entre 
# 1 e 100 (min=1 e max=100) e armazene em um vetor. Faça outra 
# função que percorra esse vetor e coloque os
# números pares em um vetor chamado pares e os números ímpares 
# em outro vetor
# chamado ímpares (essa função receberá três vetores como 
# parâmetros: o principal com
# todos os números, o vetor de pares e o vetor de ímpares). 
# Imprima os três vetores.

import random
#-----------------------funçoes------------------------
# Gerar um número aleatório entre MIN a MAX
def gerarNumAleatorio(min,max):
    return random.randint(min,max)


#repetir a escolha de numeros e guardar no vetor
def guardarVetor(numeros,par,impar):
    min = 1
    max = 100
    cont = 0
    while cont < 50 :
        n = gerarNumAleatorio(min,max)
        numeros.append(n)
        parOuImpar(n,par,impar)
        cont = cont + 1


#percorrer os numeros
def percorreNum(num):
    i = 0 
    while i < 50: 
       i = i + 1

        
#verificar se e par ou impar
def parOuImpar(n,par,impar):
    if n % 2 == 0 :
        par.append(n)
    else :
        impar.append(n)

#contar quantos pares 
def contPar(p): 
    return len(p)

#contar quantos impares
def contImpar(i):
    return len(i)

#imprimir os pares e impares
def imprimir(r1,r2,r0):
    print("---------------------------------------------")
    print("O resultado de numeros pares sao %d"%r1)
    print("O resultado de numeros impares sao %d"%r2)
    print("A quantidade todal de numeros e %d"%r0)
    print("---------------------------------------------")
    
#-----------------------main---------------------------
def main():
    numeros = []
    par = []
    impar = []
    guardarVetor(numeros,par,impar)
    percorreNum(numeros)
    r0 = len(numeros)
    r1 = contPar(par)
    r2 = contImpar(impar)
    imprimir(r1,r2,r0)
    
main()