# Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
# O resultado da soma é 77
indice = 12
soma = 0
k = 1

while k<indice:
    k+=1
    print(k)
    soma+=k
    print("SOMA:" ,soma)

print(soma)
