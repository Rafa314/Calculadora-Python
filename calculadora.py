print("Bem vindo a minha calculadora simples em Python meu primeiro projeto totalmente original ")
print("Para começarmos:")
def calculador():
    operacao = input("digite o tipo de operação que você quer calcular: adição:'+' subtração:'-' multiplicação: 'x' divisão:'/' :")
    num1 = int(input('Digite o primeiro número a ser calculado:'))
    num2 = int(input('Digite o segundo número a ser calculado:'))
    if operacao == '+':
     resultado = num1 + num2
     print('{} + {} = {}'.format(num1, num2, resultado))
    elif operacao == '-':
       resultado = num1 - num2
       print('{} - {} = {}'.format(num1, num2, resultado))
    elif operacao == '/':
        resultado = num1 / num2
        print('{} / {} = {}'.format(num1, num2, resultado))
    elif operacao == 'x':
        resultado = num1 * num2
        print('{} x {} = {}'.format(num1, num2, resultado))
calculador()

repeticao = input('Processo finalizado quer repetir? y/n:')
while repeticao == 'y':
    calculador()
    repeticao = input('Processo finalizado quer repetir? y/n:')
if repeticao == 'n':
    print('Obrigado!')
