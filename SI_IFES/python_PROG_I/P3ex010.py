#Gabaritos
gab1 = str(input("Qual foi o gabarito (A/B/C/D/E) da questão 1: ")).upper()
while gab1 != "A" and gab1 != "B" and gab1 != "C" and gab1 != "D" and gab1 != "E":
    print("Esse gabarito está errado")
    gab1 = str(input("Qual foi o gabarito (A/B/C/D/E) da questão 1: ")).upper()
gab2 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 2: ")).upper()
while gab2 != "A" and gab2 != "B" and gab2 != "C" and gab2 != "D" and gab2 != "E" :
    print("Esse gabarito esta errado")
    gab2 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 2: ")).upper()
gab3 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 3: ")).upper()
while gab3 != "A" and gab3 != "B" and gab3 != "C" and gab3 != "D" and gab3 != "E" :
    print("Esse gabarito esta errado")
    gab3 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 3: ")).upper()
gab4 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 4: ")).upper()
while gab4 != "A" and gab4 != "B" and gab4 != "C" and gab4 != "D" and gab4 != "E" :
    print("Esse gabarito esta errado")
    gab4 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 4: ")).upper()
gab5 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 5: ")).upper()
while gab5 != "A" and gab5 != "B" and gab5 != "C" and gab5 != "D" and gab5 != "E" :
    print("Esse gabarito esta errado")
    gab5 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 5: ")).upper()
gab6 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 6: ")).upper()
while gab6 != "A" and gab6 != "B" and gab6 != "C" and gab6 != "D" and gab6 != "E" :
    print("Esse gabarito esta errado")
    gab6 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 6: ")).upper()
gab7 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 7: ")).upper()
while gab7 != "A" and gab7 != "B" and gab7 != "C" and gab7 != "D" and gab7 != "E" :
    print("Esse gabarito esta errado")
    gab7 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 7: ")).upper()
gab8 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 8: ")).upper()
while gab8 != "A" and gab8 != "B" and gab8 != "C" and gab8 != "D" and gab8 != "E" :
    print("Esse gabarito esta errado")
    gab8 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 8: ")).upper()
gab9 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 9: ")).upper()
while gab9 != "A" and gab9 != "B" and gab9 != "C" and gab9 != "D" and gab9 != "E" :
    print("Esse gabarito esta errado")
    gab9 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 9: ")).upper()
gab10 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 10: ")).upper()
while gab10 != "A" and gab10 != "B" and gab10 != "C" and gab10 != "D" and gab10 != "E" :
    print("Esse gabarito esta errado")
    gab10 = str(input("Qual foi o gabarito(A/B/C/D/E) da questao 10: ")).upper()

#pedir a nota e comparar com o gabarito
pontos = 0
cont = 1
while cont < 10 :
    alternativaMarcada = str(input("Digite a alternativa que o aluno marcou: "))
    if cont == 1 :
        if alternativaMarcada == gab1 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 2:
        if alternativaMarcada == gab2 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 3 :
        if alternativaMarcada == gab3 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 4 :
        if alternativaMarcada == gab4 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 5 :
        if alternativaMarcada == gab5 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 6 :
        if alternativaMarcada == gab6 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 7 :
        if alternativaMarcada == gab7 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 8 :
        if alternativaMarcada == gab8 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 9 :
        if alternativaMarcada == gab9 :
            pontos = pontos + 1
            cont = cont + 1
    elif cont == 10 :
        if alternativaMarcada == gab10 :
            pontos = pontos + 1
            cont = cont + 1
    else:
        cont = cont + 1
print("A nota que ele tirou foi: %d"%pontos)