"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverter_string(s):
    nova_string = ''
    for i in range(len(s) - 1, -1, -1):
        nova_string += s[i]
    return nova_string


def main():
    string_original = input("Digite uma string: ")
    print("A string invertida é:", inverter_string(string_original))


if __name__ == "__main__":
    main()