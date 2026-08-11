"""
Calculadora simples de linha de comando.
Suporta soma, subtração, multiplicação e divisão.
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def main():
    print("=== Calculadora ===")
    print("Operações: + - * /")

    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite números válidos.")
        return

    operacoes = {
        "+": somar,
        "-": subtrair,
        "*": multiplicar,
        "/": dividir,
    }

    if operacao not in operacoes:
        print("Operação inválida.")
        return

    try:
        resultado = operacoes[operacao](num1, num2)
        print(f"Resultado: {resultado}")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
