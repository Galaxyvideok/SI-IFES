/* Agora você foi contratado por uma renomada casa de show de 
Colatina para fazer o programa de venda de ingressos para 10 
shows. Cada show terá uma quantidade máxima de ingressos, 
diferentes um do outro. A quantidade máxima de cada show é 
armazenada em um vetor (maxShow), respectivamente para cada 
show (use um índice para cada show). O vetor “vendas” 
armazena a quantidade de ingressos vendidos para cada show,
respectivamente. Esse vetor começa com zero para todos os 
shows. Quando uma venda é realizada em um show, a quantidade
na posição correspondente nesse vetor é somada. Você deverá
programar as 3 funções que estão faltando: 
- showsDisponíveis: imprimir na tela somente os shows 
que ainda tem vaga, ou seja, cuja venda é menor que o 
máximo para cada show. 
- realizarVenda: pedir o número do show e a quantidade de 
ingressos. Verificar se existem
vagas para este show e somar a quantidade vendida ao vetor
de vendas. Senão tiver vagas, imprimir uma mensagem de erro.
- imprimir: imprimir somente os shows que tiveram vendas.  
*/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <ctype.h>

#define INICIO "--------INICIO--------"
#define RESULTADO "-----------RESULTADO-----------"
#define CORTE "-------------------------------------"
#define MAX 1000

void showsDisponiveis(int *maxShow, int *vendas, int tamanho){
    int i;
    printf("\n%s\n", RESULTADO);
    for (i = 0; i < tamanho; i++){
        if (vendas[i] < maxShow[i]){
            printf("O show %d, atualmente, tem dispiveis: %d igressos\n",i+1,maxShow[i]);
        }
        
    }
}

int pedirDados(int desci, int *maxShow, int numShow){
    int num;
    if (desci == 1){
        do{
            printf("Digite o numero do show que voce deseja ir: ");
            scanf("%d", &num);
        } while ((num <= 0)||(num > 10));
        return num;
    }else{
        do{
            printf("Digite a quantidade de ingressos para o show %d: ", numShow);
            scanf("%d", &num);
        } while ((num <= 0)||(num > maxShow[numShow]));
        return num;
    }
}

void realizarVenda(int **maxShow, int **vendas, int tamanho){
    int numeroShow, quanti, i;
    numeroShow = pedirDados(1,*maxShow,0);
    quanti = pedirDados(1,*maxShow,numeroShow);
    for (i = 0; i < tamanho; i++){
        if (i == numeroShow){
            *maxShow[i] -= quanti;
            *vendas[i] += quanti;
        }
    }
}

void imprimir(int *vendas, int tamanho){
    int i;
    printf("\n%s\n", RESULTADO);
    for (i = 0; i < tamanho; i++){
        if (vendas[i] > 0){
            printf("A quantidade das vendas do show %d e: %d\n",i+1,vendas[i]);
        }
    }
    printf("\n%s\n", CORTE);
}

int main() { 
    SetConsoleOutputCP(65001);
    int maxShow[10] = {100,110,120,120,130,130,140,140,150,150}; 
    int vendas[10] = {0,0,0,0,0,0,0,0,0,0}; 
    int op, tamanho = 10;
    do{
        printf("\n%s\n", INICIO);
        printf("\n\t1 - Vender ingresso"); 
        printf("\n\t2 - Listar vendidos");       
        printf("\n\t0 - Sair");       
        printf("\n\tSua opção: ");       
        scanf("%d", &op); 
        switch (op){
        case 0:
            break;
        
        case 1:
            showsDisponiveis(maxShow,vendas,tamanho);
            realizarVenda(&maxShow,&vendas,tamanho);
            printf("\n%s\n", CORTE);
            break;
        
        case 2:
            imprimir(vendas,tamanho);
            break;
        
        default:
            printf("\n\n\tOpção inválida!\n");
            printf("\n%s\n", CORTE);
            break;
        }
    } while (op != 0);
}