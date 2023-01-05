#CALCULADORA COM CONDICIONAIS USANDO O WHILE

print("Calculadora")
print('digite + para adição')
print('Digite - para subtração')
print('Digite / para Divisão')
print('Digite * para multiplicação')
print('Pressione s para sair')

op = input('Qual operação deseja fazer? ')
x = int(input('Digite um valor a ser calculado '))
y = int(input('Digite outro valor a ser calculado '))

while (op != 's'):

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x,y,res))

    elif (op == '-'):
        res = x-y
        print('Resultado: {} - {} = {}'.format(x,y,res))

    elif (op == '*'):
          res = x*y
          print('Resultado: {} * {} = {}'.format(x,y,res))

    elif (op == '/'):
         res = x / y
         print('Resultado: {} / {} = {}'.format(x,y,res))

    else:
         print('Operação inválida')
    op = input('Qual operação deseja fazer? ')
    if op =='+' or op == '-' or op == '/' or op == '*':
     x = int(input('Digite um valor a ser calculado '))
     y = int(input('Digite outro valor a ser calculado '))
    print('Encerrando o programa')
