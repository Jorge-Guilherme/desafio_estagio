"""
int INDICE = 12, SOMA = 0, K = 1; 

enquanto K < INDICE faça { 
K = K + 1; 
SOMA = SOMA + K; 
} ]
imprimir(SOMA);

"""

# A tradução do código acima é:

indice, soma, k = 12, 0, 1

while k < indice:
    k += 1
    soma += k

print(soma)

# portanto a saída é 77