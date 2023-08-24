/*Implemente um algoritmo de calculadora que faça as operações de:
 Adição
 Subtração
 Divisão
 Multiplicação (usando a função da questão 3)
 Potência (usando a função da questão 4)
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define inicio "--------INICIO--------"
#define resultado "-----------RESULTADO-----------"
#define corte "-------------------------------------"


int menu(){
    int op;

    printf("\n%s\n", inicio);
    printf("\n1-ADIÇÃO\n");
    printf("\n2-SUBTRAÇÃO\n");
    printf("\n3-DIVISÃO\n");
    printf("\n4-MULTIPLICAÇÃO\n");
    printf("\n5-POTENCIA\n");
    printf("\n6-SAIR\n");
    printf("Digite a sua opção:");
    scanf("%d", &op);

    return op;
}

int pedirNum(){
    int num;
    do{
        printf("Digite um numero inteiro: ");
        scanf("%d", &num);
    } while (num < 0);
    return num;
}

void lerDados(int *num1, int *num2){
    *num1 = pedirNum();
    *num2 = pedirNum();
}

int adicao(int num1, int num2){
    int res = num1 + num2;
    return res;
}

int subtracao(int num1, int num2){
    int res = num1 - num2;
    return res;
}

int divisao(int num1, int num2) {
    int res = num1 / num2;
    return res;
}

int multiplicacao(int n1, int n2){
    int res, cont;
    cont = 0;
    res = 0;
    while(cont < n2){
        res += n1;
        cont++;
    }
    return res;
}

int potencia(int n1, int n2){
    int res, cont, valor;
    cont = 0;
    res = 0;
    valor = n1;
    while(cont < n2-1){
        valor = multiplicacao(valor, n1);
        cont++;
    }
    return valor;
}

int main() {
    
    int n1, n2, final, escolha;
    do{
        escolha = menu();
        switch (escolha){
        case 1:
            lerDados(&n1, &n2);
            final = adicao(n1, n2);
            printf("\n%s\n", resultado);
            printf("O resultado da adição de %d e %d sera: %d", n1, n2, final);
            printf("\n%s\n", corte);
            break;
        
        case 2:
            lerDados(&n1, &n2);
            final = subtracao(n1, n2);
            printf("\n%s\n", resultado);
            printf("O resultado da subtração de %d e %d sera: %d", n1, n2, final);
            printf("\n%s\n", corte);
            break;
        
        case 3:
            lerDados(&n1, &n2);
            final = divisao(n1, n2);
            printf("\n%s\n", resultado);
            printf("O resultado da divisão de %d e %d sera: %d", n1, n2, final);
            printf("\n%s\n", corte);
            break;
        
        case 4:
            lerDados(&n1, &n2);
            final = multiplicacao(n1, n2);
            printf("\n%s\n", resultado);
            printf("O resultado da multiplicação de %d e %d sera: %d", n1, n2, final);
            printf("\n%s\n", corte);
            break;
        
        case 5:
            lerDados(&n1, &n2);
            final = potencia(n1, n2);
            printf("\n%s\n", resultado);
            printf("O resultado da potencia de %d e %d sera: %d", n1, n2, final);
            printf("\n%s\n", corte);
            break;
        }
    } while (escolha != 6);
    return 0;
}