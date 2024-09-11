# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
import math

def quadrado_perfeito(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x

def pertence_fibonacci(numero):
    if numero < 0:
        return False
    return (quadrado_perfeito(5 * numero * numero + 4) or
            quadrado_perfeito(5 * numero * numero - 4))

def main():
    try:
        numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        if pertence_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, informe um número válido.")

main()