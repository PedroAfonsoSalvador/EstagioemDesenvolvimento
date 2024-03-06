"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva
um programa na linguagem que desejar onde, informado um número, ele calcule a sequência
de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a
sequência.
"""

def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        print(numero, "pertence à sequência de Fibonacci.")
    else:
        print(numero, "não pertence à sequência de Fibonacci.")

def main():
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    verifica_fibonacci(numero)

if __name__ == "__main__":
    main()