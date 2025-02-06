"""
Calculadora com while
"""

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Qual operador deseja usar? (+-/*) ')
    

    numero_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numero_validos = True

        soma = num1_float + num2_float
        subtracao = num1_float - num2_float
        divisao = num1_float / num2_float
        multiplicacao = num1_float * num2_float

    except:
        numero_validos = None

    if numero_validos is None:
        print('Um dos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print("digite apenas um operador.")
        continue

    if operador  == '+':
        print(f'O resultado é da soma de {num1_float} + {num2_float} é {soma} ')
    elif operador == '-':
        print(f'O resultado é da subtração de {num1_float} - {num2_float} é {subtracao} ')
    elif operador == '/':
        print(f'O resultado é da divisão de {num1_float} / {num2_float} é {divisao} ')
    elif operador == '*':
        print(f'O resultado é da multiplicação de {num1_float} * {num2_float} é {multiplicacao} ')
    else:
        print('Alguma coisa deu errada!')

    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break