def main():
    print("CALCULADORA PYTHON\n")

    print("[1] ADIÇÃO")
    print("[2] SUBTRAÇÃO")
    print("[3] MULTIPLICAÇÃO")
    print("[4] DIVISÃO\n")

    opcao = input()     

    num1 = int(input("Digite o primeiro número:\n"))
    num2 = int(input("Digite o segundo número:\n"))

    opcoes = {
        '1' : adicao,
        '2' : subtracao,
        '3' : multiplicacao,
        '4' : divisao,
    }

    operacao_escolhida = opcoes.get(opcao)
    if operacao_escolhida:
        print(f"Resultado: {operacao_escolhida(num1, num2)}")
    else:
        print("Opção inválida.")
    
def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Indefinido"
    else:
        return num1 / num2

main()