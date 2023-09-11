import math

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"


print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite a opção (1/2/3/4): ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == '1':
    resultado = adicao(numero1, numero2)
    print("Resultado: ", resultado)
elif opcao == '2':
    resultado = subtracao(numero1, numero2)
    print("Resultado: ", resultado)
elif opcao == '3':
    resultado = multiplicacao(numero1, numero2)
    print("Resultado: ", resultado)
elif opcao == '4':
    resultado = divisao(numero1, numero2)
    print("Resultado: ", resultado)
else:
    print("Opção inválida!")